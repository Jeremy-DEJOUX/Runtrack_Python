print('Hello')

for i in range(100):
    if (i % 5 == 0 and i % 3 == 0):
        print('FizzBuzz')
    elif (i % 5 == 0):
        print('Buzz')
    elif (i % 3 == 0):
        print('Fizz')
    else:
        print(i, ' et ni un multiple de 5, ni un multiple de 3')