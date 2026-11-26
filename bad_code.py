def calculate_total(price, quantity):
    total = price * quantity
    if total > 1000:
        print("High value order")
    else:
        print("Normal order")
    return total


def greet(name):
    message = "Hello " + name
    print(message)


def unused_function():
    x = 10
    y = 20
    return x + y


if __name__ == "__main__":
    result = calculate_total(500, 3)
    greet("Abhinav")
    print("Total:", result)
