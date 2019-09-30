#LAMBDA FUNCTIONS

add = lambda x, y: x + y

print(add(5, 7))


def double(x):
    return 2 * x

sequence = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, sequence))

print(doubled)