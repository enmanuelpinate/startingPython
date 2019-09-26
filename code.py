#VARIABLES

x = 15

price = 9.99

discount = 0.2

result = price*(1 - discount)

print(result)

name = "Carlos"

print(name)
print(name*2)

#STRING FORMATTING

name = "Juan"

print(f"Hello, {name}")

name = "Carlos"

print(f"Hello, {name}")

greeting = "Hello, {}"
with_name = greeting.format(name)
with_name = greeting.format("Rodolfo")

print(with_name)