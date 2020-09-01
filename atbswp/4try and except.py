def div50by (divisor):
    try:
        return 50 / divisor
    except ZeroDivisionError:
        print('Why you dividing by zero')

print(div50by(10))
print(div50by(12))
print(div50by(0))
print(div50by(4))