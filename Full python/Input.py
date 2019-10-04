#INPUT

size_input = input("How big is your home (in square feet): ") #input funciton is always returning string value
square_metres = int(size_input) / 10.8

print(f"{size_input} square feet is {square_metres:.2f} square metres.")

user_age = input("Enter your age: ")
years = int(user_age)
months = 12*years

print(f"Your age, {years}, is equal to {months} months.")