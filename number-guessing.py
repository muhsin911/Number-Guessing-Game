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
