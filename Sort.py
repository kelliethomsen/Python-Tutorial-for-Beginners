# https://www.youtube.com/watch?v=b8xNqP1IiU4&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=54
# sort() method   = used with lists
# sort() function = used with iterables

students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78))

grade = lambda grades:grades[1]
# students.sort(key=age)                     # sorts current list
sorted_students = sorted(students,key=grade) # sorts and creates a new list
# if you want to reverse type: sorted_students = students(key=grade, reverse=True)

for i in sorted_students:
    print(i)
