student_heights = input("Input a list of student heights: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0

for i in student_heights:
    total_height = total_height + i
print(f"Total height combined: {total_height}.")

student_count = 0

for i in student_heights:
    student_count = student_count + 1
print(f"Number of students: {student_count}.")

average_height = round(total_height / student_count)

print(f"The average height of the students is: {average_height}.")