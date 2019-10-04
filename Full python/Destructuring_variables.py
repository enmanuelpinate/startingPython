#DESTRUCTURING VARIBALES

x, y = 5, 11

friend_ages = [("Raul", 24), ("Samantha", 25), ("Jose", 30), ("Bladimir", 32)]

for name, age in friend_ages:
    print(f"{name}'s age is {age}")

head, *tail = [1, 2, 3, 4, 5, 6] #CAN also be *head, tail

print(head)
print(tail)