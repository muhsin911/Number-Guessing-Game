# Number-Guessing-Game
Number guessing game in Python 3

### Number Guessing Game

This is a simple number guessing game where the program generates a random number within a specified range, and the player tries to guess it. The number of chances the player has is calculated based on the range size, using binary search logic. Here's how the code works:

1. **Imports**:
   - `math`: Used for mathematical functions.
   - `random`: Used to generate a random number.

2. **User Input**:
   - The user is asked to input the lower and upper bounds for the number range.
   - The program then generates a random number (`x`) between these bounds.

3. **Total Chances Calculation**:
   - The number of chances the player has to guess the number is calculated using the formula:
     `math.ceil(math.log(upper-lower+1, 2))`.
     This formula determines the minimum number of guesses required to guess any number within the given range using binary search.

4. **Game Instructions**:
   - The program displays the total number of chances the user has and the range within which they need to guess the number.

5. **Game Loop**:
   - The game enters a loop, where the user is repeatedly asked to guess the number.
   - For each guess:
     - If the guess is correct, the user is congratulated, and the loop exits.
     - If the guess is too low, a hint is given ("Your guess is too low").
     - If the guess is too high, a hint is given ("Your guess is too high").
     - If the input is invalid (e.g., a non-integer), the user is prompted again.
   - The loop runs until the user guesses correctly or runs out of chances.

6. **End of Game**:
   - If the user guesses correctly, they are congratulated and told how many tries it took.
   - If they run out of chances without guessing the correct number, a message is displayed informing them that they couldn't guess the number and wishing them better luck next time.

```python
import math
import random

lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))

x = random.randint(lower, upper)

total_chances = math.ceil(math.log(upper-lower+1, 2))
print(f"You have {total_chances} chances"
      f"to guess the number between {lower} and {upper}")

count = 0
flag = False
while count < total_chances:
    count += 1
    guess = int(input("Guess a number: "))
    if x == guess:
        print(f"Congratulations! You guessed the number. in {count} tries")
        flag = True
        break
    elif x > guess:
        print("Your guess is too low")
    elif x < guess:
        print("you guess is too high")
    else:
        print("Invalid input")

if not flag:
    print(f"Sorry! You couldn't guess the number {x} in {total_chances} tries")
    print("Better luck next time!")
