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

def simulate(max_loss_streak):
    starting_bankroll = 100
    bankroll = starting_bankroll
    bet = 1
    loss_streak = 0
    round_num = 1

    # Print the rules at the top
    print("Simulation Rules:")
    print("- Player hits when hand value is 16 or less; stands on 17 and above.")
    print("- Dealer hits until reaching at least 17 (soft 17 stands).")
    print("- Martingale betting: double your bet after a loss, repeat bet on push, reset to 1 on win.")
    print(f"- Simulation stops after {max_loss_streak} consecutive losses or when bankroll hits zero.")
    print("\nRecommended Range for meaningful simulation results: 1 to 10 consecutive losses")
    print("  • 1-5: Shows normal risk scenarios")
    print("  • 6-8: Shows high-risk scenarios (likely bankroll exhaustion)")
    print("  • 9-10: Extreme scenarios (virtually impossible to reach)\n")

    print(f"Starting bankroll: {bankroll} units\n")

    deck = create_deck()

    while loss_streak < max_loss_streak and bankroll > 0:
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
            bankroll += 2 * bet   # stake + winnings
            loss_streak = 0
            next_bet = 1
        elif outcome == 'push':
            bankroll += bet       # refund stake
            next_bet = bet
        else:  # lose
            loss_streak += 1
            next_bet = bet * 2

        # print round summary
        print(
            f"Round {round_num:2d} | "
            f"Bet = {bet:3d} | "
            f"Outcome = {outcome.upper():4s} | "
            f"Bankroll = {bankroll:4d} | "
            f"Loss Streak = {loss_streak}"
        )

        bet = next_bet
        round_num += 1

    print("\nSimulation ended.")
    print(f"Final bankroll: {bankroll} units")
    print(f"Total rounds played: {round_num - 1}")

if __name__ == '__main__':
    try:
        n = int(input("Enter the number of consecutive losses to stop on: ").strip())
        if n < 1:
            raise ValueError
    except ValueError:
        print("Invalid input. Defaulting to 5 consecutive losses.\n")
        n = 5

    simulate(n)
