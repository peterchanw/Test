a = 5
b = 2

# Error handling
try:
    print('resource Open')
    print(a/b)
    k = int(input('Enter a number '))
    print(k)

except ValueError as e:
    print('Invalid Input')

except Exception as e:
    print('Run time error - ', e)

finally:
    print('resource Closed')

print('Bye')

