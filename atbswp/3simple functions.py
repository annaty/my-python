def hello(name):
    print('Hello ' + name)

hello('Anna')
hello('Bob')

def letterCount(word):
    print(word + ' has ' + str(len(word)) + ' letters in it')

letterCount('coconut')
letterCount('crabapple')

#keyword arguments are the ones that you pass to a function with their name
print('Hello', end='   !!') #removes the default new line that python does between print statements
print('dog', 'cat', 'horse', sep='??')