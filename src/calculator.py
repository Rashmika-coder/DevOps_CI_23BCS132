def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b

def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    return a ** b




if __name__ == "__main__":
    print("DevOps CI Calculator")
    print("2 + 3 =", add(2, 3))
    print("10 - 4 =", subtract(10, 4))
    print("5 * 6 =", multiply(5, 6))
    print("20 / 4 =", divide(20, 4))