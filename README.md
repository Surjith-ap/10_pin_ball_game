# Ten-Pin Bowling Score Calculator

A Python program that calculates the total score for a ten-pin bowling game based on a string representation of the game.


## How to Play

Run the program and enter your bowling game as a string of characters representing each roll. The program will calculate and display your total score.

### Running the Program

```bash
python ten_pin.py
```

---

## Input Format

Enter your bowling game using the following symbols:

| Symbol | Meaning |
|--------|---------|
| `X` | Strike (knocked down all 10 pins on first roll) |
| `/` | Spare (knocked down remaining pins on second roll) |
| `0-9` | Number of pins knocked down |
| `-` | Gutter ball (0 pins knocked down) |

### Important Notes:
- Remove spaces between frames when entering your game
- The 10th frame may have up to 3 rolls if you get a strike or spare
- Enter the complete game string in one line

---

## Scoring Rules

### Strike (X)
- **Score**: 10 + next 2 rolls
- **Example**: Frame with `X` followed by rolls of 7 and 3 = 10 + 7 + 3 = **20 points**

### Spare (/)
- **Score**: 10 + next 1 roll
- **Example**: Frame with `7/` followed by roll of 9 = 10 + 9 = **19 points**

### Open Frame
- **Score**: Sum of 2 rolls
- **Example**: Frame with `9-` = 9 + 0 = **9 points**

### 10th Frame Special Rule
- If you get a strike or spare in the 10th frame, you get bonus rolls
- Strike: 2 bonus rolls
- Spare: 1 bonus roll
- Maximum possible score: **300** (perfect game - 12 strikes)

---

## How the Code Works

### Step 1: Parse the Game String

The `ten_pin()` function converts each character into numeric roll values:

```python
rolls = []
for c in game_string:
    if c == 'X':
        rolls.append(10)
    elif c == '-':
        rolls.append(0)
    elif c == '/':
        previous = rolls[-1]
        rolls.append(10 - previous)
    else:
        rolls.append(int(c))
```

**Example**: `'X7/9-'` becomes `[10, 7, 3, 9, 0]`

### Step 2: Score Each Frame

The program iterates through exactly 10 frames and calculates scores based on the type of frame:

```python
for frame in range(1, 11):
    if rolls[roll_index] == 10:
        # Strike: 10 + next two rolls
        frame_score = 10 + rolls[roll_index + 1] + rolls[roll_index + 2]
        roll_index += 1
    
    elif rolls[roll_index] + rolls[roll_index + 1] == 10:
        # Spare: 10 + next 1 roll
        frame_score = 10 + rolls[roll_index + 2]
        roll_index += 2
    
    else:
        # Open frame: sum of two rolls
        frame_score = rolls[roll_index] + rolls[roll_index + 1]
        roll_index += 2
    
    total_score += frame_score
```

### Key Variables:
- `rolls`: List of all numeric roll values
- `roll_index`: Current position in the rolls list
- `frame_score`: Points scored in current frame
- `total_score`: Cumulative score across all frames

---

## Usage

### Interactive Mode

1. Run the program:
   ```bash
   python ten_pin.py
   ```

2. Enter your game when prompted:
   ```
   Enter the sequence of the bowling game (or 'quit' to exit): X7/9-X-88/-6XXX81
   ```

3. View your score:
   ```
   ------------------------------------------------------------
   TOTAL SCORE: 167
   ------------------------------------------------------------
   ```

4. Enter another game or type `quit` to exit

### Programmatic Usage

You can also import and use the function directly:

```python
from ten_pin import ten_pin

score = ten_pin('XXXXXXXXXXXX')  # Perfect game
print(score)  # Output: 300
```

---

## Examples

### Example 1: Perfect Game
**Input**: `XXXXXXXXXXXX`
- All strikes (12 total, including bonus rolls in 10th frame)
- **Score**: 300

### Example 2: All Spares
**Input**: `5/5/5/5/5/5/5/5/5/5/5`
- Each frame is a spare (5 pins, then knock down remaining 5)
- **Score**: 150

### Example 3: All 9s (No Spares)
**Input**: `9-9-9-9-9-9-9-9-9-9-`
- Each frame: 9 pins on first roll, miss on second
- **Score**: 90

### Some more Test Cases
**Input 1 Mixed Game**: `X7/9-X-88/-6XXX81`
- **Score**: 167

**Input 2 Strike in last frame**: `9-9-9-9-9-9-9-9-9-XXX`
- **Score**: 111

**Input 3 Spare in last frame**: `9-9-9-9-9-9-9-9-9-5/5`
- **Score**: 96

**Input 4 Strike followed by spare**: `X5/9-9-9-9-9-9-9-9-`
- **Score**: 111

**Input 5 Single strike, rest open**: `X9-9-9-9-9-9-9-9-9-`
- **Score**: 100

**Input 6 All misses**: `--------------------`
- **Score**: 0

## Error Handling

The program handles common errors:

- **Invalid characters**: Non-bowling symbols in input
- **Insufficient rolls**: Game string doesn't have enough rolls
- **Empty input**: No game string provided

---

## Files in This Project

- `ten_pin.py` - Main program with scoring logic and user interface
- `sample.py` - Example script showing roll parsing
- `README.md` - This documentation file

---

## Requirements

- Python 3.6 or higher
- No external dependencies required

---

