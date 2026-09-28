# numbers = [10, 25, 40, 55, 70, 15]

# for number in numbers:
#     if number > 50:
#         print(number)

# numbers = [10, 25, 40, 55, 70, 15]

# count = 0

# for number in numbers:
#     if number > 50:
#         count +=1

# print(count)

# numbers = [10, 15, 20, 25, 30]

# def count_even(numbers):
#     count = 0
#     for number in numbers:
#         if number % 2 == 0: 
#             count +=1
#     return count

# result = count_even(numbers)
# print(result)

# marks = {
#     "Ravi" : 45,
#     "Aman" : 75,
#     "Priya" : 85,
#     "Rahul" : 30
# }

# def count_passed_students(marks):
#     count = 0
#     for student, mark in marks.items():
#         if mark >= 50:
#             count += 1
#     return count

# result = count_passed_students(marks)
# print(result)


# def read_file(filename):
#         try:
#             with open(filename) as file:
#                  content = file.read()
#             return content
#         except FileNotFoundError:
#              return("File not found")

# result = read_file("notes.txt")
# print(result)

# marks = {
#     "Ravi": 45,
#     "Aman": 75,
#     "Priya": 85,
#     "Rahul": 30
# }

# def get_passed_students(marks):
#     passed_students = []

#     for student, mark in marks.items():
#         if mark >= 50:
#             passed_students.append(student)
#     return(passed_students)

# result = get_passed_students(marks)
# print(result)

# def read_file(filename):
#     try:
#         with open(filename) as file:
#             content = file.read()
#         return content
#     except FileNotFoundError:
#         return("File not found")

# result = read_file("notes.txt")
# print(result)

# marks = {
#     "Ravi": 45,
#     "Aman": 75,
#     "Priya": 85,
#     "Rahul": 30
# }

# def get_grade_report(marks):
#     report = {}
#     for student, mark in marks.items():
#         if mark >= 80:
#             report[student] = "Excellent"
#         elif mark >= 50:
#             report[student] = "Pass"
#         else:
#             report[student] = "Fail"
#     return report

# result = get_grade_report(marks)
# print(result)

# students = {
#     "Ravi": [45, 60, 75],
#     "Aman": [80, 90, 85],
#     "Priya": [35, 40, 45],
#     "Rahul": [70, 55, 65]
# }

# def get_passed_students(students):
#     passed_students = []
#     for student, mark in students.items():
#         if sum(mark) / 3 >= 50:
#             passed_students.append(student)
#     return passed_students

# result = get_passed_students(students)
# print(result)

# students = {
#     "Ravi" : [45, 60, 75],
#     "Aman" : [80, 90, 85],
#     "Priya" : [35, 40, 45],
#     "Rahul" : [70, 55, 65]
# }
# def get_top_students(students):
#     top_students = {}
#     for student, mark in students.items():
#         average = sum(mark) / 3
#         if average >= 70:
#             top_students[student] = average
#     return top_students

# result = get_top_students(students)
# print(result)

# students = {
#     "Ravi": [45, 60, 75],
#     "Aman": [80, 90, 85],
#     "Priya": [35, 40, 45],
#     "Rahul": [70, 55, 65]
# }

# def get_student_averages(students):
#     student_averages = {}
#     for student, mark in students.items():
#         average = sum(mark) / 3
#         student_averages[student] = average
#     return student_averages

# result = get_student_averages(students)
# print(result)

# students = {
#     "Ravi": [45, 60, 75],
#     "Aman": [80, 90, 85],
#     "Priya": [35, 40, 45],
#     "Rahul": [70, 55, 65],
#     "Karan": [90, 85, 95]
# }

# def get_result(students):
#     count = 0
#     passed_students = []
#     for student, mark in students.items():
#         average = sum(mark) / 3
#         if average >= 50:
#             count +=1
#             passed_students.append(student)
#     return count, passed_students

# result = get_result(students)
# print(result)

# students = {
#     "Ravi": [45, 60, 75],
#     "Aman": [80, 90, 85],
#     "Priya": [35, 40, 45],
#     "Rahul": [70, 55, 65],
#     "Karan": [90, 85, 95]
# }

# def get_statistics(students):
#     total_students = len(students)
#     passed_students = 0
#     passed_students_name = []
#     for student, mark in students.items():
#         average = sum(mark) / 3
#         if average >= 50:
#             passed_students +=1
#             passed_students_name.append(student)
#     return total_students, passed_students, passed_students_name

# total_students, passed_students, passed_students_name = get_statistics(students)
# print(total_students)
# print(passed_students)
# print(passed_students_name)

# inventory = {
#     "Laptop" : [5, 60000],
#     "Phone" : [10, 25000],
#     "Keyboard" : [20, 1500],
#     "Mouse" : [30, 800],
#     "Monitor" : [8, 12000]
# }

# def calculate_inventory(inventory):
#     total_different_products = len(inventory)
#     total_value = 0
#     total_items = 0
#     for items, values in inventory.items():
#         total_items += 1
#         total_value

# product = [5, 60000]

# quantity = product[0]
# price = product[1]

# print(quantity)
# print(price)
# print(quantity * price)

# products = {
#     "Laptop": [5, 60000],
#     "Phone": [10, 25000]
# }

# for item, values in products.items():
#     print(item)
#     print(values[0])
#     print(values[1])
#     total_items += values[0]
#     total_value += values[0] * values[1]
#     return total_different_products, total_items, total_value\

# inventory = {
#     "Laptop": [5, 60000],
#     "Phone": [10, 25000],
#     "Keyboard": [20, 1500],
#     "Mouse": [30, 800],
#     "Monitor": [8, 12000]
# }

# def calculate_inventory(inventory):
#     total_numbers = len(inventory)
#     total_items = 0
#     total_values = 0
#     for items, values in inventory.items():
#         total_items += values[0]
#         total_values += values[0] * values[1]
#     return total_numbers, total_items, total_values

# total_numbers, total_items, total_values = calculate_inventory(inventory)
# print(total_numbers)
# print(total_items)
# print(total_values)

# inventory = {
#     "Laptop": [5, 60000],
#     "Phone": [10, 25000],
#     "Keyboard": [20, 1500],
#     "Mouse": [30, 800],
#     "Monitor": [8, 12000]
# }

# def get_stock_report(inventory):
#     low_stock_products = []
#     total_values = 0
#     for items, values in inventory.items():
#         if values[0] < 10:
#             low_stock_products.append(items)
#             total_values += values[0] * values[1]
#     return low_stock_products, total_values

# low_stock_products, total_values = get_stock_report(inventory)
# print(low_stock_products)
# print(total_values)