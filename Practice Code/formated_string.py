first = "Renan"
last = "Genova"

full = first + " " + last #concatenation of strings 
print(full)


first = "Renan"
last = "Genova" 
full = f"{first} {last}" #using f-string for string interpolation
print(full)

test = f"5 + 10 = {5 + 10}" #using f-string to evaluate an expression inside the string
print(test)