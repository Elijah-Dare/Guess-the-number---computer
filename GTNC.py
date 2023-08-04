import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print("Sorry you have guessed too low, try again")
        elif guess > random_number:
            print("Sorry You have guessed too high, try again")
            
            
    print(f'Yes, Congratulations, you have guessed the right number {random_number} correctly')
        
guess(1000)