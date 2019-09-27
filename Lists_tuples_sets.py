#LISTS, TUPLES AND SETS

l = ["Bob", "Nanda", "Tebayo"] #You CAN modify values inside a list. List keep order when printing.

t = ("Bob", "Nanda", "Tebayo") #You CAN NOT modify values inside a tuple. Tuples keep order when printing.

s = {"Bob", "Nanda", "Tebayo"} #You CAN NOT have duplicated values in a set, it means you can't have "Bob" twice.
                               #Sets don't keep order when printing.

print(l[0])
l.append("Luis")
print(l)
l.remove("Bob")
print(l)

s.add("Holis")
print(s)

friends = {"Bob", "Nanda", "Tebayo"}
abroad_friends = {"Bob", "Tebayo"}

local_friends = friends.difference(abroad_friends)
print(local_friends)

new_friends = {"Holis", "Bebe"}

all_friends = new_friends.union(friends)
print(all_friends)

ciencia = {"Holis", "Que", "Mas"}
artes = {"Bien", "Holis", "Ytu", "Mas"}

both = ciencia.intersection(artes)
print(both)
