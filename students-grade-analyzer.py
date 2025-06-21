# Write a python program to enter students' names and grades 
# (out of 100) (the number of 
# students should be decided by the user) and the 
# program will do the following:
# 1- Prints students names and grades
# 2- Prints the average grade of the class
# 3- Prints the highest grade earned (Student name and grade)
# 4- Prints the count of students who passed (grade >= 60)

# You have to use loops, lists, functions and recursive functions.
# Your code should have the following functions display_student_summary
# , get_avg_grade, get_heighest_grade, count_passed

def get_highest_grade(grades):
    if len(grades)==1:
        return grades[0]
    max=get_highest_grade(grades[1:])
    if grades[0]>max:
        return grades[0]
    else:
        return max
def count_passed(grades):
    passed=0
    for grade in grades:
        if grade >= 60:
            passed +=1
    return passed
def get_avg_grade(grades):
    if len(grades)==0:
        return 0
    total=0
    for grade in grades:
            total +=grade
    return total/ len(grades)
def display_student_summary(names, grades):
    for name, grade in zip(names, grades):
        print(f"My name is {name} and my score is: {grade}")
def isnumber(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
def Students_grade():
    names=[]
    grades=[]
    while True:
        students=int(input("Enter your number of students: "))
        if students>0:
            break
        else:
            print("Please enter a valid number.")

    for student in range (students):
        name = input("Please enter your name: ")
        while True:
            grade_in =input("Please enter your grade between [0-100]: ")
            if isnumber(grade_in):
                grade = int(grade_in)
                if 0 <= grade <= 100 :
                    break
                else:
                    print("Invalid GRADE! Please enter a number between 0 and 100.")
            else:
                print("Invalid GRADE! Please enter a number between 0 and 100.")
        names.append(name)
        grades.append(grade)
    display_student_summary(names, grades)
    print(f"My average grade for this class is: {get_avg_grade(grades)}")
    print(f"the count of students passed: {count_passed(grades)}")
    max_grade = get_highest_grade(grades)
    name_max = grades.index(max_grade)
    print(f"The highest grade is: {max_grade} by student {names[name_max]}")
Students_grade()