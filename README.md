# Blackjack Simulation with Martingale Betting Strategy

A Python simulation of Blackjack using a single deck with the Martingale betting system to analyze the effectiveness and risks of this popular gambling strategy.

## Overview

This simulation implements a complete Blackjack game with the following features:
- Single deck (52 cards) with automatic reshuffling when cards run low
- Standard Blackjack rules with proper Ace handling
- Martingale betting strategy implementation
- Detailed round-by-round tracking and statistics

## Game Rules

### Blackjack Rules
- **Player Strategy**: Hits on hand value ≤ 16, stands on 17+
- **Dealer Strategy**: Hits until reaching at least 17 (soft 17 stands)
- **Card Values**: Number cards (2-10) = face value, Face cards (J,Q,K) = 10, Ace = 11 or 1 (whichever is better)
- **Winning Conditions**: 
  - Player wins if dealer busts or player's hand is closer to 21
  - Dealer wins if player busts or dealer's hand is closer to 21
  - Push (tie) if both hands have equal value

### Martingale Betting Strategy
- Start with a base bet of 1 unit
- **After a loss**: Double the bet for the next round
- **After a win**: Reset bet to 1 unit
- **After a push**: Keep the same bet amount

## Features

- **Automatic Deck Management**: Reshuffles when fewer than 15 cards remain
- **Bankroll Tracking**: Starts with 100 units, tracks gains/losses
- **Loss Streak Monitoring**: Configurable stopping condition based on consecutive losses
- **Detailed Output**: Round-by-round breakdown showing bet amount, outcome, bankroll, and loss streak

## Installation

No external dependencies required. The simulation uses only Python standard library modules:
- `random` (for deck shuffling)
- `collections.deque` (for efficient deck operations)

## Usage

Run the simulation:

```bash
python blackjack_martingale.py
```

You'll be prompted to enter the maximum number of consecutive losses before the simulation stops. Enter a positive integer or press Enter to use the default value of 5.

### Example Output

```
Simulation Rules:
- Player hits when hand value is 16 or less; stands on 17 and above.
- Dealer hits until reaching at least 17 (soft 17 stands).
- Martingale betting: double your bet after a loss, repeat bet on push, reset to 1 on win.
- Simulation stops after 5 consecutive losses or when bankroll hits zero.

Starting bankroll: 100 units

Round  1 | Bet =   1 | Outcome = WIN  | Bankroll =  101 | Loss Streak = 0
Round  2 | Bet =   1 | Outcome = LOSE | Bankroll =  100 | Loss Streak = 1
Round  3 | Bet =   2 | Outcome = WIN  | Bankroll =  102 | Loss Streak = 0
Round  4 | Bet =   1 | Outcome = PUSH | Bankroll =  102 | Loss Streak = 0
Round  5 | Bet =   1 | Outcome = LOSE | Bankroll =  101 | Loss Streak = 1
...

Simulation ended.
Final bankroll: 95 units
Total rounds played: 23
```

## Key Insights

This simulation helps demonstrate:
1. **Martingale Limitations**: Even with a "winning" strategy, consecutive losses can quickly deplete bankroll
2. **Risk vs. Reward**: Small frequent wins vs. potential large losses
3. **Bankroll Requirements**: The exponential growth of bet sizes during losing streaks
4. **Statistical Reality**: House edge persists regardless of betting strategy

## Customization

You can modify the simulation by adjusting:
- **Starting bankroll**: Change `starting_bankroll` in the `simulate()` function
- **Base bet amount**: Modify the initial `bet = 1` value
- **Player strategy**: Update the `play_player()` function logic
- **Deck size**: Modify `create_deck()` for multiple decks
- **Reshuffling threshold**: Change the `< 15` cards condition

## Files

- `blackjack_martingale.py`: Main simulation script
- `README.md`: This documentation file

## Warning

This simulation is for educational purposes only. The Martingale betting system does not overcome the house edge in gambling and can lead to significant losses. This tool should not be used as guidance for actual gambling decisions.

## License

This project is open source and available under the MIT License.
