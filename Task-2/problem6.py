c = int(input("Please enter the number of the students and thier scores: "))
studata = []
for lista in range(0,c):
    new_student = input("")
    new_student = new_student.split()
    studata.append(new_student)
student_choice = input("")
for lista1 in range(0,c):
    if str(student_choice) == str(studata[lista1][0]):
        average = (int(studata[lista1][1]) + int(studata[lista1][2]) + int(studata[lista1][3]))/3
        print(average)