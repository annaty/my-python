total = 0
for num in range(101):
    total = total + num
print(total)

completesum = 50
for i in range(51):
    if i < 50:
        smallsum = i + (100-i)
        completesum = completesum + smallsum 
print(completesum)

for i in range (5, -1, -2): # (upper bound, lower bound, interval)
    print('only ' + str(i) + ' seconds left')

for i in range (5, 10, 5): # (lower bound, upper bound, interval)
    print('only ' + str(i) + ' seconds left')