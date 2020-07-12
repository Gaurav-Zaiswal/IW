from datetime import date
import re
import csv

from students import Student

email_re = "^\\w+([-+.']\\w+)*@\\w+([-.]\\w+)*\\.\\w+([-.]\\w+)*$"

course_switcher = {
    1: 'Web Development',
    2: 'Android Development',
    3: 'iOS Developement',
    4: 'C/C++'
}
print('==========================================================')
print('         Welcome to ADVANCED TECHNICAL WORKSHOP           ')
print('==========================================================')

# input for inquiry
reg_or_course = ''
while not reg_or_course in [1,2,3]:
    try:
        reg_or_course = int(input('Enter\n'
                                  '1. To register for course\n'
                                  '2. To inquiry:\n'
                                  '3. To Log in\n'))
    except ValueError:
        print('Oppsss... an integer value was expected!\n')

# if reg_or_course == 1 do registration
if reg_or_course == 1:
    reg_details = {}

    print('Choose a course you want to register for:\n')
    course = ''
    while course not in [1, 2, 3, 4]:
        for key, value in course_switcher.items():
            print(f'{key}. {value}')
        try:
            course = int(input())
        except ValueError:
            print('Oppsss.. an integer value was expected!\n')

    if course == 1:
        reg_details['course'] = 'Web Development'
    elif course == 1:
        reg_details['course'] = 'Android Development'
    elif course == 1:
        reg_details['course'] = 'iOS Developement'
    else:
        reg_details['course'] = 'C/C++'

    # input and validatioin for student's name
    s_name = ''
    name_flag = False
    while not name_flag == True:
        s_name = input('Enter your full name: ').upper()
        # name validation
        for _ in s_name:
            if ord(_) not in range(65, 123):
                if ord(_) != 32:
                    print('Opps... Name can have A-Z or a-z with whitespaces.')
                    name_flag = False
                    break

            name_flag = True
    reg_details['student_name'] = s_name

    # input and validation for student's email
    s_email = ''
    email_flag = False
    while not email_flag == True:
        s_email = input('Enter your email address: \n'
                        'Email has to be unique and cannot be modified later: ').lower()
        if (re.search(email_re, s_email)):
            reg_details['email'] = s_email
            email_flag = True

        else:
            print("Invalid Email...")

    # make instance of Student
    s1 = Student(
        student_name=reg_details['student_name'],
        email=reg_details['email'],
        course=reg_details['course'],
    )

    print('\n')
    print('==========================================================')
    print('                 CONFIRM registration                     ')
    print('==========================================================')
    confirm = input("Hit any key to confirm or cancel by pressing 'Q' or 'q' key: ")
    if confirm in ['q', 'Q']:
        print('\nRegistration has been cancelled!')
    else:
        print('You have been registered successfully\n'
              'Here, is your course details:\n')
        course_detail = s1.confirm_registration()
        for key, value in course_detail.items():
            print(f'{key} : {value}')


elif reg_or_course == 2:
    # inquiry part tomorrow
    print('We offer following courses:\n')
    for key, value in course_switcher.items():
        print(f'{key}. {value}')

elif reg_or_course == 3:
    print('==========================================================')
    print('                         Log in                           ')
    print('==========================================================')

    email2 = input('Enter your email address: ')
    file = email2.replace('@', '').replace('.', '')
    filename = 'registrations/' + file + '.csv'
    does_user_exists = Student(file=filename) # checks whether the email exists or not
    if does_user_exists == True:
        print('\n\n==========================================================')
        print('                   Welcome Back Student!                    ')
        print('==========================================================')

        # let user choose any action after loggin in
        user_action = ''
        while not user_action in [1, 2, 3, 4, 5]:
            '''User can view their dashboard, take assessment, make payment, edit profile, or can quit the course'''
            try:
                user_action = int(input('Enter\n'
                                        '1. Check your course status\n'
                                          '2. To make payment\n'
                                          '3. To take assessment exam\n'
                                          '4. To edit your Name\n'
                                           '5. To delete your profile: '))
            except ValueError:
                print('Oppsss.. an integer value was expected!\n')

        # check status
        if user_action == 1:
            user_status = Student.check_student_status(filename)
            print('\n==========================================================\n')
            print('Your account status:\n')
            for key, value in user_status.items():
                print(f'{key} : {value}')
            print('\n==========================================================')

        # make payment
        elif user_action == 2:
            # pay = Student.make_payment(filename)
            amt_flag = ''
            amt = ''
            while not amt_flag in [1, 2]:
                try:
                    amt_flag = int(input('Enter\n'
                                              '1. To pay 10000\n'
                                              '2. To pay 20000:\n'))
                    if amt_flag == 1:
                        amt = 10000
                    elif amt_flag == 2:
                        amt = 20000
                except ValueError:
                    print('Oppsss.. an integer value was expected!\n')

            pay = Student.make_payment(file=filename, amount=amt)
            print('\n')
            if pay == True:
                print('Payment was successfull')
            else:
                print('Payment was not accepted. Make sure you have due payments.')

        # take assessment exam
        elif user_action == 3:
            print('\n==========================================================')
            print("    If you have due payments, you won't get any grades.    ")
            print('==========================================================')
            a_marks = ''
            while not a_marks in range(0, 120):
                try:
                    a_marks = int(input('Enter students marks: '))
                except ValueError:
                    print('Oppsss.. an integer value was expected!\n')
            exam_response = Student.take_assessment(file=filename, marks=a_marks)
            if exam_response == True:
                print('Result has been recorded. See them on dashboard.')
            elif exam_response == False:
                print('Result was not recorded.')
            else:
                print(exam_response)

        # update student's name
        elif user_action == 4:
            s_name = ''
            name_flag = False
            while not name_flag == True:
                s_name = input('Enter your full name: ').upper()
                # name validation
                for _ in s_name:
                    if ord(_) not in range(65, 123) or ord(_) == 32:
                        print('Opps... Name can have A-Z or a-z with whitespaces.')
                        name_flag = False
                        break

                    name_flag = True
            # reg_details['student_name'] = s_name
            updated_name = Student.update_name(cls, file=filename, new_name=s_name)
            if updated_name == True:
                print('Your name is updated successfully!')
            elif updated_name == False:
                print('Name could not be updated!')

        # remove user
        elif user_action == 5:
            remove_user = Student.remove_user(file=filename)
            if remove_user == True:
                print('\n==========================================================')
                print('         Profile has been deleted successfully')
                print('\n==========================================================')

            else:
                print('Some error occured. Make sure user exists.')


    else:
        print('Email Not Found!\n'
              "Make sure email is valid...")

