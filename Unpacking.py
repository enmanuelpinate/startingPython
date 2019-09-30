#UNPACKING ARGUMENTS

def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    
    return total

def apply(*args, operator):
    if operator == "*":
        return multiply(*args) #Unpacking
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator"

print(apply(1, 2, 5, 7, operator="+"))