#LIST COMPREHENSIONS

numbers = [1, 2, 5]
double = [num * 2 for num in numbers]

friends = ["Jose", "Luis", "Samuel", "Samantha", "Sosa"]
start_s = [friend for friend in friends if friend.startswith("S")]

print(start_s)