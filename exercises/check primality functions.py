def checkIfPrime():
    number = int(input('Give me a number:'))
    if number % 1 == 0 and number % number == 0 and number % 2 != 0:
        print('Your number is a prime number')
    
    else:
        print('Your number is not a prime number')

checkIfPrime()

def get_integer(help_text="Give me a number: "):
    return int(input(help_text))

age = get_integer("Tell me your age: ")
school_year = get_integer()
if age > 15:
    print("You are over the age of 15")
print("You are in grade " + str(school_year))