n = int(input())
numbers = []
for i in range(n):
    element = input()
    numbers.append(element)

for i in range (0, len(numbers)):
    numbers[i] = int(numbers[i])
#    if "-" in numbers[i]:
#        numbers[i].strip("-")
#        print(numbers[i])
#        numbers[i] = 0 - int(numbers[i]) 
#    else:
#        numbers[element] = int(numbers[element])

sum = 0
for number in numbers:
    sum += number 

mean = sum / n
print(mean)