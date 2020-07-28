import random

wordlist = ["python", "java", "kotlin", "javascript"]
theword = wordlist[random.randint(0, 3)]
theword_length = len(theword)
print("H A N G M A N")
print("Guess the word " + theword[:3] + ((theword_length - 3)* "-") + ":")
guess = input()

if guess == theword:
    print("You survived!")
else:
    print("You are hanged!")
