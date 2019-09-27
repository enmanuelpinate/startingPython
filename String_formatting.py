#STRING FORMATTING

name = "Juan"

print(f"Hello, {name}")

name = "Carlos"

print(f"Hello, {name}")

greeting = "Hello, {}"
with_name = greeting.format(name)
with_name = greeting.format("Rodolfo")

print(with_name)