def display_students_summary(number_of_students,name,grade):
    print("Names: \t\t\t\t Grades:")
    for i in range(number_of_students):
        print(name[i], "\t", grade[i])


def get_avg_grade(number_of_students,grade):
    avg_grade=0
    sum_of_grade=0
    for i in range (number_of_students):
        sum_of_grade=sum_of_grade+grade[i]
    avg_grade=sum_of_grade/number_of_students
    return avg_grade

def get_heighest_grade(number_of_students,name,grade):
    heighst_grade=0
    student_of_heighst_grade=""
    for i in range (number_of_students):
        if grade[i]>heighst_grade:
            heighst_grade=grade[i]
            student_of_heighst_grade=name[i]
    print( "the heighst grade is for ",student_of_heighst_grade,"of grade is ",heighst_grade)

def count_passed(number_of_students,grade,count_students,i):
   
   if number_of_students==0:
     return count_students
   else :
     if grade[i]<60 :
       count_students -=1
       i=i+1
     return count_passed(number_of_students-1,grade,count_students,i)
   
#hon lmain
num_of_students=int(input("Hello teacher ! enter the number of your students\n"))



student_name=[]
student_grade=[]



print("enter the student name and grade")

for i in range(num_of_students):
    student_name.append(input().capitalize())
    student_grade.append(float(input()))
    while student_grade[i]>100 or student_grade[i]<0:
            print("invalid grade")
            student_grade.append(float(input()))

#displaying the functions
display_students_summary(num_of_students,student_name,student_grade)
print("The avg grade of the students :")
print(get_avg_grade(num_of_students,student_grade))
get_heighest_grade(num_of_students,student_name,student_grade)
print("The number of students who passed are :")
print(count_passed(num_of_students,student_grade,num_of_students,0))
