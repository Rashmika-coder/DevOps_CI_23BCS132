import math

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(a)


if __name__ == "__main__":
    print("DevOps CI Calculator")
    print("2 + 3 =", add(2, 3))
    print("10 - 4 =", subtract(10, 4))
    print("5 * 6 =", multiply(5, 6))
    print("20 / 4 =", divide(20, 4))
    print("2 ^ 3 =", power(2, 3))