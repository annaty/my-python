name = ''
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break #stops the infinite while loop
print('Thanks')

spam = 0
while spam < 5:
    spam += 1
    if spam == 3:
        continue # when spam is 3, skip the rest of the rest of the clause and continue the loop
    print('spam is ' + str(spam))