def fib(number):
    if number <= 1:
        result = number
        print(result)
    else:
        result = fib(number - 1) + fib(number - 2)
        print(result)

    return result


fib(7)
