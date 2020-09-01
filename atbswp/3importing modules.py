import random
num = random.randint(25, 50)
print(num)

import random, sys, os, math

from random import * #import everything from the module
#it's better to use just import random
#use the random.whatever notation

import sys
sys.exit() #the program will terminate on that line

import pyperclip
pyperclip.copy('blablabla')
testpc = pyperclip.paste()
print(testpc)