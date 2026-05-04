# My "Hello World" equivalent! My first ever project. 
# The code is, of course, not up to par, and there are a lot of improvements to be made to it, but this is and was my starting point.
# If you have advice for me, I am absolute more than open for every bit I can learn!

first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
address = '123 Main Street'
address += ', Apartment 4B'

# Subject Work Experience and work info

experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
position = 'Data Analyst'
salary = 75000

# Specific Employee Variables and Definitions

employee_age = 28
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
employee_code = "DEV-2026-JD-001"
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'

# Slice Operations

department = employee_code[0:3]
year_code = employee_code[4:8]
initials = employee_code[9:11]
last_three = employee_code[-3:]

# Print Operators -> conjoining all print operators advisable (?) or other optimisation solution

print(employee_info)
print(experience_info)
print(department)
print(employee_card)
print(year_code)
print(initials)
print(last_three)
