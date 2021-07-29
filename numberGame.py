import random
print("Number Guessing Game")

number=random.randint(1,9)
chances=0
print("Guess a number between 1 and 9")
while chances<5:
    guess=int(input("Enter your guess :"))
    if guess==number:
        print("CONGRATULATIONS YOU WON")
        break
    elif guess<number:
        print("Your guess is low, please try a higher number than",guess)
    else :
        print("Your guess is high, please try a lower number than",guess)
    chances+=1

if not chances<5:
    print("YOU LOST")
    print("The number is",number)