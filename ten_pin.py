def ten_pin(game_string):
    rolls = []

    # Converting symbols into numeric roll values for fast processing
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

    total_score = 0
    roll_index = 0

    # Score exactly 10 frames, one frame at a time procees only upto 10 frames
    for frame in range(1, 11):

        if rolls[roll_index] == 10:
            # score calculation for a Strike -> 10 + next two rolls
            frame_score = (10 + rolls[roll_index + 1] + rolls[roll_index + 2])

            total_score += frame_score
            roll_index += 1

        elif rolls[roll_index] + rolls[roll_index + 1] == 10:
            # score calculation for a Spare -> 10 + next 1 roll
            frame_score = (10 + rolls[roll_index + 2])

            total_score += frame_score
            roll_index += 2

        else:
            # score calculation for an Open frame -> sum of two rolls
            frame_score = (rolls[roll_index] + rolls[roll_index + 1])

            total_score += frame_score
            roll_index += 2

    return total_score


def main():
    
    while True:
        try:
            game_string = input("\nEnter the sequence of the bowling game (or 'quit' to exit): ").strip()
        
            if game_string.lower() in ['quit', 'exit', 'q']:
                print("\nThanks for using the Ten-Pin Bowling Score Calculator!")
                break
            
            if not game_string:
                print("Error: Please enter a valid game string.")
                print("Example: X X X X X X X X X XXX")
                print("Example: 9- 9- 9- 9- 9- 9- 9- 9- 9- 9-")
                print("Example: 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5")
                continue
        
            score = ten_pin(game_string)
            
            print("\n" + "-" * 60)
            print(f"TOTAL SCORE: {score}")
            print("-" * 60)
            
        except IndexError:
            print("Error: Invalid game format. Make sure you have enough rolls.")
        except ValueError:
            print("Error: Invalid character in game string.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
