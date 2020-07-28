#guess the number game
import random

print('What is your name?')
name = input()

print('Well ' + name + ', I am thinking of a number between 1 and 20.')
random = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess > random:
        print('Your guess is too high.')
        guess
    elif guess < random:
        print('Your guess is too low.')
        guess
    else:
        break

if guess == random:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(random))
