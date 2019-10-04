#ERROS

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor can not be 0.")

    return dividend / divisor

grades = []
try:
    average = divide(sum(grades), len(grades))
    print(f"The average grade is {average}.")
except ZeroDivisionError:
    print("There are not grades yet in your list.")