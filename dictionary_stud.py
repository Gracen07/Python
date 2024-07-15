students = []
n = int(input("Enter the number of students: "))
for i in range(n):
    print(f"Enter details for student {i+1}:")
    name = input("Name: ")
    roll_no = input("Roll No: ")
    total_mark = float(input("Total Marks: "))
    student_dict = {
        'name': name,
        'roll_no': roll_no,
        'total_mark': total_mark    }
    students.append(student_dict)
highest_mark = float(0)
highest_mark_student = None    
for student in students:
    if student['total_mark'] > highest_mark:
        highest_mark = student['total_mark']
        highest_mark_student = student    
print("\nDetails of the student with the highest total marks:")
print(f"Name: {highest_mark_student['name']}")
print(f"Roll No: {highest_mark_student['roll_no']}")
print(f"Total Marks: {highest_mark_student['total_mark']}")
