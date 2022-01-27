# r stands for read
# w stands for write (changfe the information)
# a stands for append (add new information)
# r+ stabnds for read and write
employee_file = open("employees.text", "r")

# print(employee_file.readable())
# print(employee_file.read())
# print(employee_file.readline()) # reads first line
# print(employee_file.readline()) # reads second line

for employee in employee_file.readlines():
    print(employee)
employee_file.close()