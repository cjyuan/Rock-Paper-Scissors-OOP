### 1. Overview

Joe wants to build a system that facilitates competitions between two or more automated players in variations of the Rock–Paper–Scissors (RPS) game.  
The system must be extensible so that new competition rules, scoring mechanisms, and player strategies can be added without modifying existing code.

Initially, competitions will be run locally via a command-line interface (CLI). In the long term, the system should be reusable for web-based competitions,
where users can submit their own automated players.

### 2. Universal Game Rules

The following rules apply to all competitions:
  1. On each turn, every player must choose exactly one move: **Rock**, **Paper**, or **Scissors**.
  2. Move outcomes are defined as:
    - Rock defeats Scissors
    - Scissors defeats Paper
    - Paper defeats Rock
  3. If two players choose the same move, the result is a tie for that matchup.

### 3. Competition-Specific Rules

Different competition variants are expected to define different sets of rules.
Each competition variant should encapsulate its own behavior and rule logic, allowing new competition types to be introduced without modifying existing ones.

These additional rules are intentionally open-ended and may affect any aspect of the competition, including but not limited to:
- How long the competition lasts (e.g., 10 turns per player)
- How scores are calculated (e.g., winning two consecutive turns yields bonus points)
- How winners are determined (e.g., the first player to score 100 points wins)
- What constraints apply to player moves (e.g., a player may play Rock at most 20 times during the competition)
- How many players participate

The system must allow new competition variants to be added by defining new competition types,
without requiring changes to the competition framework or core game engine.

### 4. Player Interaction Requirements

Each automated player must interact with the competition through a well-defined interface.

#### 4.1. Competition Start Notification
- Each player must be notified before the competition begins.

#### 4.2. Turn Execution
- On each turn, a player is asked to choose a move.
- The player must be given read-only access to the following info of all players:
  - their previous moves
  - their current score

#### 4.3. Competition End Notification
- Each player must be notified when the competition ends.

### 5. Player Metadata

Each player must have:
- A name
- A short textual description

### 6. Design and Extensibility Goals
- The system should support the addition of new competition variants and new player implementations.
- The core game logic should be reusable for future web-based deployment.

### 7. Implementation
To demonstrate the design, the implementation must include the following:
- At least two distinct competition variants
- Several different player implementations
- A game engine responsible for facilitating and managing a competition
- A command-line interface (CLI) program that uses the game engine to run the competitions and display the results
