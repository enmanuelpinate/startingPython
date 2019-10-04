#FUNCTIONS

def hello():
    print("Hello!")

hello()

def add(x, y):
    result = x + y
    print(result)

add(58, 83)

def names(name):
    print(f"Hello {name}")

names("Bob")

def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("Can't divide by 0")

divide(5, 10)

#DEFAULTS VALUES

def add(x, y=8):
    return x + y

result = add(5)
print(result)