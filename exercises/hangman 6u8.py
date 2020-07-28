import random
wordlist = ["python", "java", "kotlin", "javascript"]
theword = wordlist[random.randint(0, 3)]
theword_length = len(theword)
theword_hidden = list(theword_length * "-")
theword_list = list(theword)
guess_list = []

print("H A N G M A N")
for i in range(0, 8):
    print("\n" + "".join(theword_hidden))
    letter_input = input("Input a letter:")
    tries = 8
    if letter_input in theword_list:
        counter = 0
        for letter in theword_list:
            counter += 1
            if letter_input == letter:
                theword_hidden[counter-1] = letter_input
    elif letter_input not in theword:
        tries -= 1
        print("No such letter in the word")
    elif letter_input in guess_list:
        tries -= 1
        print("No improvements")
    guess_list.append(letter_input)

if "".join(theword_hidden) == theword:
    print("\nYou guessed the word!\nYou survived")
else:
    print("You are hanged!")