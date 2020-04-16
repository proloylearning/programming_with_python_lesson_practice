from statistics import mean as m

admins = {'Python': 'Pass123@', 'user2': 'pass2'}

studentDict = {'Jeff': [78.00, 88.00, 93.00],
               'Alex': [92.00, 76.00, 88.00],
               'Sam': [89.00, 92.00, 93.00]}


def enter_grades():
    name_to_enter = input('Student Name: ')
    grade_to_enter = input('Grade: ')

    if name_to_enter in studentDict:
        print('Adding Grade...')
        studentDict[name_to_enter].append(float(grade_to_enter))
    else:
        print('Student does not exist.')

    print(studentDict)


def remove_student():
    name_to_remove = input('What student to remove?: ')
    if name_to_remove in studentDict:
        print('removing student...')
        del studentDict[name_to_remove]

    print(studentDict)


def student_avgs():
    for eachStudent in studentDict:
        grade_list = studentDict[eachStudent]
        avg_grade = m(grade_list)

        print(eachStudent, 'has an average grade of:', avg_grade)


def main():
    print("""
    Welcome to Grade Central

    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit
    """)

    action = input('What would you like to do today? (Enter a number) ')

    if action == '1':
        enter_grades()
    elif action == '2':
        remove_student()
    elif action == '3':
        student_avgs()
    elif action == '4':
        exit()
    else:
        print('No valid choice was given, try again')


login = input('Username: ')
password = input('Password: ')

if login in admins:
    if admins[login] == password:
        print('Welcome,', login)
        while True:
            main()
    else:
        print('Invalid password, will detonate in 5 seconds!')
else:
    print('Invalid username, calling the FBI to report this')
