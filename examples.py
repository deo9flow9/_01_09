def factorial(n):
    if n <= 1:
        return 1
    else:
        print(n / 0)
        return n * factorial(n - 1)

try:
    print(factorial(1000))
except (RecursionError, ZeroDivisionError):
    print("This program calculate factorials that large or division error")
