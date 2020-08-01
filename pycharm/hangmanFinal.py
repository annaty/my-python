import random
wordlist = ["python", "java", "kotlin", "javascript"]
theword = wordlist[random.randint(0, 3)]
theword_length = len(theword)
theword_hidden = list(theword_length * "-")
theword_list = list(theword)
guess_list = []
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "w", "v", "x", "y", "z"]

def runTheGame():
    print("H A N G M A N")
    decision = input("""Type "play" to play the game, "exit" to quit:""")
    if decision == "play":
        game()
    elif decision == "exit":
        return
def game():
    tries = 8
    while tries != 0:
        print("\n" + "".join(theword_hidden))
        letter_input: str = input("Input a letter:")

        if len(letter_input) != 1:
            print("You should input a single letter")
        elif letter_input not in alphabet:
            print("It is not an ASCII lowercase letter")
        elif letter_input in theword_hidden or letter_input in guess_list:
            print("You already typed this letter")
        elif letter_input in theword_list:
            counter = 0
            for letter in theword_list:
                counter += 1
                if letter_input == letter:
                    theword_hidden[counter-1] = letter_input
        elif letter_input not in theword:
            tries -= 1
            print("No such letter in the word")
        guess_list.append(letter_input)

    if "".join(theword_hidden) == theword:
        print("You guessed the word!\nYou survived!")
        runTheGame()
    else:
        print("You are hanged!")
        runTheGame()

runTheGame()