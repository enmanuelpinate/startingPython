#LOOPS

number = 7

while True:
    user_input = input("Would you like to play? (Y/n) ")

    if user_input == "n":
        break

    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif number - user_number in (1, -1):
        print("You were off by one!")
    else:
        print("Sorry, it's wrong!")

    user_input = input("Would you like to play? (Y/n) ")


grades = [1, 2 ,3, 5, 80, 1000, 90, 2]
total = 0 #sum(grades) does better in this case
amount = len(grades)

for grade in grades:
    total += grade

print(total / amount)