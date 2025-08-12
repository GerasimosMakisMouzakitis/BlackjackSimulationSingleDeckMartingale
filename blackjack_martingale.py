import random
from collections import deque

# Card values for blackjack
CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

def create_deck():
    """Return a shuffled single deck of 52 cards."""
    deck = [card for card in CARD_VALUES] * 4
    random.shuffle(deck)
    return deque(deck)

def hand_value(hand):
    """Calculate the best blackjack hand value, adjusting Aces."""
    total = sum(CARD_VALUES[c] for c in hand)
    aces = hand.count('A')
    while total > 21 and aces:
        total -= 10
        aces   -= 1
    return total

def deal_initial_hands(deck):
    """Deal two cards to player and dealer."""
    return [deck.popleft(), deck.popleft()], [deck.popleft(), deck.popleft()]

def play_player(deck, hand):
    """Player hits on total ≤ 16, stands on 17+."""
    while hand_value(hand) <= 16:
        hand.append(deck.popleft())
    return hand

def play_dealer(deck, hand):
    """Dealer hits until reaching at least 17 (soft 17 stands)."""
    while hand_value(hand) < 17:
        hand.append(deck.popleft())
    return hand

def determine_outcome(player, dealer):
    """Return 'win', 'lose', or 'push' for two completed hands."""
    pv, dv = hand_value(player), hand_value(dealer)
    if pv > 21:
        return 'lose'
    if dv > 21 or pv > dv:
        return 'win'
    if pv == dv:
        return 'push'
    return 'lose'

def simulate(max_loss_streak, betting_strategy='martingale'):
    starting_bankroll = 100
    bankroll = starting_bankroll
    bet = 1
    loss_streak = 0
    win_streak = 0
    round_num = 1
    
    # Track loss and win streak frequencies (using defaultdict for any streak length)
    from collections import defaultdict
    loss_streak_counts = defaultdict(int)
    win_streak_counts = defaultdict(int)
    
    # Track total outcomes
    total_wins = 0
    total_losses = 0
    total_pushes = 0

    # Print the rules at the top
    print("Simulation Rules:")
    print("- Player hits when hand value is 16 or less; stands on 17 and above.")
    print("- Dealer hits until reaching at least 17 (soft 17 stands).")
    
    if betting_strategy == 'martingale':
        print("- Martingale betting: double your bet after a loss, repeat bet on push, reset to 1 on win.")
        print(f"- Simulation stops after {max_loss_streak} consecutive losses or when bankroll hits zero.")
    else:  # flat betting
        print("- Flat betting: always bet 1 unit regardless of outcome.")
        print(f"- Simulation stops after {max_loss_streak} consecutive losses or when bankroll hits zero.")
    
    print("\nRecommended Range for meaningful simulation results: 1 to 10 consecutive losses")
    print("  • 1-5: Shows normal risk scenarios")
    print("  • 6-8: Shows high-risk scenarios (likely bankroll exhaustion)")
    print("  • 9-10: Extreme scenarios (virtually impossible to reach)\n")

    print(f"Starting bankroll: {bankroll} units")
    print(f"Betting strategy: {betting_strategy.capitalize()}\n")

    deck = create_deck()

    while bankroll > 0 and loss_streak < max_loss_streak:
        # reshuffle when deck is low
        if len(deck) < 15:
            deck = create_deck()

        # place bet
        bankroll -= bet

        # initial deal
        player, dealer = deal_initial_hands(deck)

        # player's turn
        player = play_player(deck, player)

        # dealer's turn (only if player hasn't busted)
        if hand_value(player) <= 21:
            dealer = play_dealer(deck, dealer)

        # determine outcome
        outcome = determine_outcome(player, dealer)

        # payout/refund and next bet logic
        if outcome == 'win':
            total_wins += 1
            # Record the loss streak that just ended (if any)
            if loss_streak > 0:
                loss_streak_counts[loss_streak] += 1
            # Record the win streak that just ended (if any) when next loss occurs
            win_streak += 1
            bankroll += 2 * bet   # stake + winnings
            loss_streak = 0
            
            # Set next bet based on strategy
            if betting_strategy == 'martingale':
                next_bet = 1
            else:  # flat betting
                next_bet = 1
                
        elif outcome == 'push':
            total_pushes += 1
            bankroll += bet       # refund stake
            next_bet = bet
        else:  # lose
            total_losses += 1
            # Record the win streak that just ended (if any)
            if win_streak > 0:
                win_streak_counts[win_streak] += 1
            win_streak = 0
            loss_streak += 1
            
            # Set next bet based on strategy
            if betting_strategy == 'martingale':
                next_bet = bet * 2
            else:  # flat betting
                next_bet = 1

        # print round summary
        player_cards_str = ', '.join(player)
        dealer_cards_str = ', '.join(dealer)
        player_value = hand_value(player)
        dealer_value = hand_value(dealer)
        
        print(
            f"Round {round_num:2d} | "
            f"Bet = {bet:3d} | "
            f"Player: [{player_cards_str}] = {player_value} | "
            f"Dealer: [{dealer_cards_str}] = {dealer_value} | "
            f"Outcome = {outcome.upper():4s} | "
            f"Bankroll = {bankroll:4d} | "
            f"Loss Streak = {loss_streak}"
        )

        bet = next_bet
        round_num += 1

    # Record any final streaks that didn't end
    if loss_streak > 0:
        loss_streak_counts[loss_streak] += 1
    if win_streak > 0:
        win_streak_counts[win_streak] += 1

    print("\nSimulation ended.")
    print(f"Final bankroll: {bankroll} units")
    print(f"Total rounds played: {round_num - 1}")
    
    # Print outcome totals
    total_rounds = round_num - 1
    print(f"\nOutcome Summary:")
    print(f"  Total wins: {total_wins} ({total_wins/total_rounds*100:.1f}%)")
    print(f"  Total losses: {total_losses} ({total_losses/total_rounds*100:.1f}%)")
    print(f"  Total pushes: {total_pushes} ({total_pushes/total_rounds*100:.1f}%)")
    print(f"  Total rounds: {total_rounds}")
    
    # Print streak frequency analysis
    print(f"\nLoss Streak Frequency Analysis:")
    total_loss_streaks = sum(loss_streak_counts.values())
    if total_loss_streaks > 0:
        max_consecutive_losses = max(loss_streak_counts.keys())
        print(f"  Maximum consecutive losses achieved: {max_consecutive_losses} (limit was {max_loss_streak})")
        # Show all streak lengths from 1 to maximum achieved
        for streak_length in range(1, max_consecutive_losses + 1):
            count = loss_streak_counts.get(streak_length, 0)
            percentage = (count / total_loss_streaks) * 100 if count > 0 else 0.0
            print(f"  {streak_length} consecutive loss{'es' if streak_length > 1 else ''}: {count} times ({percentage:.1f}%)")
        print(f"  Total loss streaks: {total_loss_streaks}")
    else:
        print("  No loss streaks occurred during this simulation.")
        
    print(f"\nWin Streak Frequency Analysis:")
    total_win_streaks = sum(win_streak_counts.values())
    if total_win_streaks > 0:
        max_consecutive_wins = max(win_streak_counts.keys())
        print(f"  Maximum consecutive wins achieved: {max_consecutive_wins}")
        # Show all streak lengths from 1 to maximum achieved
        for streak_length in range(1, max_consecutive_wins + 1):
            count = win_streak_counts.get(streak_length, 0)
            percentage = (count / total_win_streaks) * 100 if count > 0 else 0.0
            print(f"  {streak_length} consecutive win{'s' if streak_length > 1 else ''}: {count} times ({percentage:.1f}%)")
        print(f"  Total win streaks: {total_win_streaks}")
    else:
        print("  No win streaks occurred during this simulation.")

if __name__ == '__main__':
    # Get betting strategy choice
    print("Select betting strategy:")
    print("1. Martingale (double bet after loss)")
    print("2. Flat (always bet 1 unit)")
    
    try:
        strategy_choice = int(input("Enter your choice (1 or 2): ").strip())
        if strategy_choice == 1:
            betting_strategy = 'martingale'
        elif strategy_choice == 2:
            betting_strategy = 'flat'
        else:
            raise ValueError
    except ValueError:
        print("Invalid input. Defaulting to Martingale strategy.\n")
        betting_strategy = 'martingale'
    
    # Get loss streak limit
    try:
        n = int(input("Enter the number of consecutive losses to stop on: ").strip())
        if n < 1:
            raise ValueError
    except ValueError:
        print("Invalid input. Defaulting to 5 consecutive losses.\n")
        n = 5

    simulate(n, betting_strategy)
