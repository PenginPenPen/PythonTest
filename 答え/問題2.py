x  = int(input())
for i in range(1, x):
    if i <= 50:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    else:
        if i % 3 == 0 and i % 5 == 0:
            print("!FizzBuzz")
        elif i % 3 == 0:
            print("!Buzz")
        elif i % 5 == 0:
            print("!Fizz")
        else:
            print(i)