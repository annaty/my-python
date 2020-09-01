# .upper(), .lower()
# .isupper(), .islower()
# we can string methods
'Hello'.upper().isupper() #True

# .isalpha() = True if a str contains only letters AND is not blank
# .isalnum() = True if a str contains letters and numbers AND is not blank
# .isdecimal() = True if a str contains only numbers
# .isspace() = True if a str contains only whitespaces
# .istitle() = True if a str contains words that all start with majuscules 

# .startswith('str'), .endswith('str')

# .join(a list of strings)
print(', '.join(['one', 'two', 'three']))
print('\n\n'.join(['one', 'two', 'three']))

# .split(), the default value in the brackets is ' '
print('No way, that\'s not possible '.split())
print('No way, that\'s not possible '.split('t'))

# .ljust(), .rjust(), .center() make the string the length of the argument, and positionit
print('Hello'.ljust(20, 'p'))
print('Hello'.rjust(20, 'p'))
print('Hello'.center(20, 'p'))

# .lstrip(), .rstrip(), .strip() removes the repeated characters on the sides of a str
print('       x       '.strip())
print('catcatcatcatdogcatcat'.strip('tac'))

# .replace('str', 'str') replaces 1st string, with the second

import pyperclip
pyperclip.copy('Hello!!!!!!!!') #copy to the clipboard

pyperclip.paste() #returns what's in the clipboard

name = 'Bob'
place = 'Pinapple Street'
time = '6 pm'
food = 'cake'
# %s = conversion specifier
print('Hello %s, you are invited to a party at %s at %s. Please bring %s.' \
%(name, place, time, food)) 