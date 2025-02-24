import sys

try:
    x = int(input('x: '))
    y = int(input('y: '))
except ValueError:
    print('Error: input must be integer')
    sys.exit(1)

try:
    result = x/y
except ZeroDivisionError:
    print('Error: cannot divide by 0')
    sys.exit(1)
print(result)