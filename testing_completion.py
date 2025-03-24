def fibonacci(n):
    fib_sequence = [0, 1]
    if n <= 1:
        return fib_sequence[n]

    for i in range(2, n + 1):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
        print(fib_sequence[i])

    return fib_sequence[n]

fibonacci(10)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))