# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
total_height=0
for height in student_heights:
    total_height += height
    print(total_height)

#Write your code below this row 👇

number_of_student=0
for student in student_heights:
    number_of_student += 1
# total_height=sum(student_heights)
# number_of_student=len(student_heights)
avarage_height=round(total_height / number_of_student)
print(avarage_height)


