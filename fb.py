for i in range (1, 23+1):
    if i % 15 ==0:
        print("FizzBuzz")
    elif i % 3 ==0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(f'{i}')
