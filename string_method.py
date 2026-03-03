course = " Python for Beginners"

print(course.upper())
print(course.lower())
print(course.title())
print(course.find("Python")) #returns the index of the first occurrence of the substring
print(course.replace("Beginners", "Everyone")) #replaces a substring with another substring
print("for" in course) #returns a boolean indicating if the substring is found in the string
print (course.strip()) #removes leading and trailing whitespace from the string
print("renan" not in course) #returns a boolean indicating if the substring is not found in the string