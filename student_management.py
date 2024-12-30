def student():
    print('Welcome to Student Management System.\n1. Add Student Details.\n2. View Student Details.\n3. Delete Student Details.\n4. Exit.')

    students = []
    while True:
        choice = int(input('Enter the choice(1/2/3/4): '))
        if choice not in [1,2,3,4]:
            print('The choice choosen is invalid. Please choose a valid one.')
        else:
            if (choice == 1):
                name = input('Enter the name of the student: ')
                marks = int(input('Enter the total marks of the student (max 1000): '))
                attendence = float(input('Enter the attendence percentage of the student: '))
                grade = input('Enter the grade of the student: ')
                students.append({'name': name, 'marks': marks, 'attendence': attendence, 'grade': grade})
            elif (choice == 2):
                if (len(students) == 0):
                    print('There is no entries of students.')
                else:
                    for stud in students:
                        print(f'Name: {stud['name']}\nMarks: {stud['marks']}\nAttendence: {stud['attendence']}%\nGrade: {stud['grade']}')
                        print('------- * -------')
            elif (choice == 3):
                delete = input('Enter name of the student to delete: ')
                for item in students:
                    if (item['name'] == delete):
                        students.remove(item)
                        print('The entry is removed successfully.')
                        break
            elif (choice == 4):
                print('Thanks for using our Student Management System. Have a great day!!')
                break

student()