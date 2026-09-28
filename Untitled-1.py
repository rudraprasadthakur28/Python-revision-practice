# file = open("notes.txt")
# content = file.read()
# print(content)
# file.close()

# with open("notes.txt") as file:
#     content = file.read()
#     print(content)

# with open("notes.txt") as file:
#     line = file.readline()
#     print(line)

# with open("notes.txt") as file:
#     line = file.readlines()
#     print(line)

# with open("practice.txt", "w") as file:
#     file.write("I am learning Python.\n" \
#     "I want to become a backend developer.")

# with open("practice.txt") as file:
#     file.write("\n I am practicing everyday.")

# with open("practice.txt", "a") as file:
#     file.write("\nI will build projects.")

# with open("practice.txt") as file:
#     content = file.read()
#     if "Python" in content:
#         print("Python found")
#     else:
#         print("Python not found")

# with open("practice.txt") as file:
#     content = file.read()
#     if "Java" in content:
#         print("Java found")
#     else:
#         print("Java not found")

# with open("practice.txt") as file:
#     content = file.read()
#     content = content.lower()
#     if "python" in content:
#         print("Python found")
#     else:
#         print("Python not found")

# with open("practice.txt") as file:
#     content = file.read()
#     content = content.replace("Python", "Java")
# with open("practice.txt", "w") as file:
#     file.write(content)

# with open("practice.txt") as file:
#     content = file.read()
# with open("backup.txt", "w") as file:
#     file.write(content)

# with open("practice.txt") as file:
#     contents = file.readlines()

# line_number = 0

# for content in contents:
#     line_number += 1

#     if "Python" in content:
#         print(f"Python is found in line {line_number}")

# import os

# os.rename("practice.txt", "newfiles.txt")

# import os

# os.remove("test.txt")

# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except ValueError:
#     print("Invalid number")

# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     divide = a / b
#     print(divide)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except ValueError:
#     print("Invalid input")

try:
    number = int(input("Enter a number: "))
    print(number * 2)
except ValueError:
    print("Invalid input")
else:
    print("Number is valid")
finally:
    print("Program finished")
