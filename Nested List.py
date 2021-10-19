#Given the names and grades for each student in a class of n
# students, store them in a nested list and print the name(s) of 
# any student(s) having the second lowest grade.
# If there are multiple students with the second lowest grade, 
#order their names alphabetically and print each name on a new line.

students_info = []
second_lowest_students=[]

n = int(input())

if n >= 2 and n <= 5:

    for i in range(n):

        name = input()
        score = float(input())
        students_info.append([name,score])

    sorted_score = sorted(list(set([x[1] for x in students_info])))
    second_lowest = sorted_score[1]

    for student in students_info:

        if second_lowest == student[1]:
            second_lowest_students.append(student[0])
    
    for student in sorted(second_lowest_students):
        print(student)

else:
    quit()