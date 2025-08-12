# Blackjack Simulation with Dual Betting Strategies

A comprehensive Python simulation of Blackjack using a single deck with support for both Martingale and Flat betting strategies to analyze their effectiveness and risks.

## Overview

This simulation implements a complete Blackjack game with the following features:
- Single deck (52 cards) with automatic reshuffling when cards run low
- Standard Blackjack rules with proper Ace handling
- **Dual betting strategies**: Martingale and Flat betting
- **Enhanced card display**: Shows player and dealer cards for each round
- **Comprehensive statistics**: Win/loss/push totals, streak frequency analysis
- **Complete streak tracking**: Displays all consecutive win/loss patterns up to maximum achieved
- Detailed round-by-round tracking with full transparency

## Game Rules

### Blackjack Rules
- **Player Strategy**: Hits on hand value ≤ 16, stands on 17+
- **Dealer Strategy**: Hits until reaching at least 17 (soft 17 stands)
- **Card Values**: Number cards (2-10) = face value, Face cards (J,Q,K) = 10, Ace = 11 or 1 (whichever is better)
- **Winning Conditions**: 
  - Player wins if dealer busts or player's hand is closer to 21
  - Dealer wins if player busts or dealer's hand is closer to 21
  - Push (tie) if both hands have equal value

### Betting Strategies

#### 1. Martingale Strategy
- Start with a base bet of 1 unit
- **After a loss**: Double the bet for the next round
- **After a win**: Reset bet to 1 unit
- **After a push**: Keep the same bet amount

#### 2. Flat Betting Strategy
- **Consistent bet**: Always bet 1 unit regardless of outcome
- **Simple approach**: No bet adjustments based on wins or losses
- **Lower risk**: Eliminates exponential loss exposure

## Features

- **Dual Betting Strategies**: Choose between Martingale (progressive) and Flat (constant) betting
- **Enhanced Card Display**: Shows actual cards dealt to player and dealer each round
- **Automatic Deck Management**: Reshuffles when fewer than 15 cards remain
- **Bankroll Tracking**: Starts with 100 units, tracks gains/losses throughout
- **Configurable Loss Limits**: Set maximum consecutive losses before stopping
- **Comprehensive Statistics**: 
  - Win/Loss/Push totals and percentages
  - Complete streak frequency analysis (wins and losses)
  - Maximum consecutive streaks achieved vs. limits set
- **Detailed Round Output**: Shows bet, cards, hand values, outcome, bankroll, and streak status

## Installation

No external dependencies required. The simulation uses only Python standard library modules:
- `random` (for deck shuffling and card dealing)
- `collections.deque` (for efficient deck operations)
- `collections.defaultdict` (for dynamic streak frequency tracking)

## Usage

Run the simulation:

```bash
python blackjack_martingale.py
```

Run the simulation:

```bash
python blackjack_martingale.py
```

The program will prompt you to:
1. **Select betting strategy**: Choose between Martingale (1) or Flat betting (2)
2. **Set consecutive loss limit**: Enter maximum consecutive losses before stopping

### Example Output

```
Select betting strategy:
1. Martingale (double bet after loss)
2. Flat (always bet 1 unit)
Enter your choice (1 or 2): 1
Enter maximum consecutive losses (default 5): 8

Simulation Rules:
- Player hits when hand value is 16 or less; stands on 17 and above.
- Dealer hits until reaching at least 17 (soft 17 stands).
- Martingale betting: double your bet after a loss, repeat bet on push, reset to 1 on win.
- Simulation stops after 8 consecutive losses or when bankroll hits zero.

Starting bankroll: 100 units

Round  1 | Bet =   1 | Player: [K, 7] = 17 | Dealer: [9, 8] = 17 | Outcome = PUSH | Bankroll =  100 | Loss Streak = 0
Round  2 | Bet =   1 | Player: [A, Q] = 21 | Dealer: [10, 6] = 16 | Outcome = WIN  | Bankroll =  101 | Loss Streak = 0
Round  3 | Bet =   1 | Player: [6, 9, 8] = 23 | Dealer: [K, 7] = 17 | Outcome = LOSE | Bankroll =  100 | Loss Streak = 1
Round  4 | Bet =   2 | Player: [J, 5] = 15 | Dealer: [A, K] = 21 | Outcome = LOSE | Bankroll =   98 | Loss Streak = 2
...

Simulation ended.
Final bankroll: 87 units
Total rounds played: 156

Outcome Summary:
  Total wins: 72 (46.2%)
  Total losses: 69 (44.2%)
  Total pushes: 15 (9.6%)
  Total rounds: 156

Loss Streak Frequency Analysis:
  Maximum consecutive losses achieved: 8 (limit was 8)
  1 consecutive loss: 18 times (40.9%)
  2 consecutive losses: 12 times (27.3%)
  3 consecutive losses: 7 times (15.9%)
  4 consecutive losses: 4 times (9.1%)
  5 consecutive losses: 2 times (4.5%)
  6 consecutive losses: 0 times (0.0%)
  7 consecutive losses: 0 times (0.0%)
  8 consecutive losses: 1 times (2.3%)
  Total loss streaks: 44

Win Streak Frequency Analysis:
  Maximum consecutive wins achieved: 5
  1 consecutive win: 23 times (51.1%)
  2 consecutive wins: 12 times (26.7%)
  3 consecutive wins: 6 times (13.3%)
  4 consecutive wins: 3 times (6.7%)
  5 consecutive wins: 1 times (2.2%)
  Total win streaks: 45
```

## Key Insights

This simulation helps demonstrate:

### Martingale Strategy Analysis
1. **Exponential Risk Growth**: Bet sizes double with each consecutive loss (1, 2, 4, 8, 16, 32...)
2. **Bankroll Requirements**: Need substantial funds to survive longer losing streaks
3. **Limited Gain vs. Unlimited Loss**: Small frequent wins vs. potential catastrophic losses
4. **House Edge Persistence**: Mathematical disadvantage remains regardless of betting pattern

### Flat Betting Strategy Analysis
1. **Consistent Risk**: Every bet is the same size, limiting exposure
2. **Slower Bankroll Depletion**: Losses accumulate linearly, not exponentially
3. **Clearer Win Rate Impact**: Results directly reflect the underlying game probabilities
4. **Streak Tolerance**: Can survive longer consecutive losing streaks

### Statistical Insights
- **Complete Streak Analysis**: See exactly how often different streak lengths occur
- **Maximum vs. Limit Comparison**: Understand whether you hit your risk tolerance or ran out of money
- **Win/Loss Distribution**: Observe the natural variance in blackjack outcomes
- **Strategy Comparison**: Direct comparison of risk profiles between betting systems

## Customization

You can modify the simulation by adjusting:
- **Starting bankroll**: Change `starting_bankroll` in the `simulate()` function (default: 100 units)
- **Base bet amount**: Modify the initial `bet = 1` value for different unit sizes
- **Player strategy**: Update the `play_player()` function for different hitting/standing rules
- **Dealer rules**: Modify dealer logic in the simulation loop
- **Deck size**: Modify `create_deck()` for multiple decks or different card distributions
- **Reshuffling threshold**: Change the `< 15` cards condition for deck management
- **Consecutive loss limits**: Adjust maximum streak limits for different risk tolerances

## Files

- `blackjack_martingale.py`: Main simulation script
- `README.md`: This documentation file

## Warning

**This simulation is for educational purposes only.** 

- The Martingale betting system does not overcome the house edge in gambling and can lead to significant losses
- Flat betting also cannot overcome the mathematical disadvantage built into casino games
- Past results do not predict future outcomes in gambling
- This tool should not be used as guidance for actual gambling decisions
- Gambling can be addictive and lead to financial problems

**Always gamble responsibly and within your means.**

## License

This project is open source and available under the MIT License.
