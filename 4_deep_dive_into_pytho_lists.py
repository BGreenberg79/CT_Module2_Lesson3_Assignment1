# Task 1 Filter out student

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

# Will use pop and append methods to isolate Jane for being below 80 grade. Remove and append would work as well.

students.pop(-2)
grades.pop(-2)
activities.pop(-2)
struggling_students=[]
struggling_students.append("Jane")
struggling_students.append(78)
struggling_students.append("Art")
print(struggling_students)

# Task 2 Add remaining students to new list
# Will use copy method to add students from original list into new students_approved list, making it easier to change eiother the original list or its clone without affecting the other

students_approved = students.copy()
grades_approved = grades.copy()
activities_approved = activities.copy()

# To be better safe than sorry I also copied the grades and activities of the approved students into new lists. A better solution down the road for this assignment is Python dictionaries!

# Task 3 Print the students_approved list

print(students_approved)