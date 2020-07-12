import datetime
import csv
import os

class Student:
    fee = 20000
    course_list = ['Web Development', 'Android Development', 'iOS Developement', 'C/C++']
    duration = 3 # duration is in months
    total_marks = 120
    pass_marks = 80

    def __init__(self, **kwargs):
        # print(kwargs[course])
        self.student_dashboard = {}
        self.due_payment = 20000
        self.installment_count_remained = 2
        self.assesment_status = 'not taken'  # possible values: 'pass', 'fail', 'not taken'
        self.has_completed = False

        for arg in kwargs:
            # print(arg, kwargs[arg])
            if arg == 'student_name':
                self.name = kwargs[arg]
                # print(self.name)
            if arg == 'email':
                self.email = kwargs[arg]
                file = kwargs['email'].replace('@', '').replace('.', '')
                self.filename = 'registrations/' + file + '.csv'

            if arg == 'course':
                self.course = kwargs[arg]

            if arg == 'joining_date':
                self.joining_date = kwargs[arg]
            else:
                self.joining_date = datetime.date.today()

            # setting file name using student's email address
            # file = kwargs['email'].replace('@', '').replace('.', '')
            # self.filename = 'registrations/' + file + '.csv'

    def confirm_registration(self):
        # save registration details in a csv file when this method is called
        self.student_dashboard["Student's Name"] = self.name
        self.student_dashboard["Student's Email"] = self.email
        self.student_dashboard['Enroll On'] = self.joining_date
        self.student_dashboard['Enrolled Course'] = self.course
        self.student_dashboard['Due Payment'] = self.due_payment
        self.student_dashboard['Remaining Installment'] = self.installment_count_remained
        self.student_dashboard['Assessment Status'] = self.assesment_status
        self.student_dashboard['Course Status'] = 'not completed'  # other possible value - 'completed'


        # saving as csv file
        with open(self.filename, mode='w', newline='') as students_file:
            fieldnames = [
                  "Student's Name",
                  "Student's Email",
                  'Enroll On',
                  'Enrolled Course',
                  'Due Payment',
                  'Remaining Installment',
                  'Assessment Status',
                  'Course Status'
            ]
            student_writer = csv.DictWriter(students_file, fieldnames=fieldnames, dialect='excel')

            student_writer.writeheader()
            student_writer.writerow({
                "Student's Name" : self.name,
                "Student's Email" : self.email,
                'Enroll On' : self.joining_date,
                'Enrolled Course' : self.course,
                'Due Payment' : self.due_payment,
                'Remaining Installment' : self.installment_count_remained,
                'Assessment Status' : self.assesment_status,
                'Course Status' : 'not completed',
            })

        return self.student_dashboard
        # return True

    @classmethod
    def does_user_exists(cls, file):
        # returns true if user with give filename exists
        return os.path.exists(file)

    @classmethod
    def check_student_status(cls, file):
        with open(file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            # print(csv_reader)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                return row

    @classmethod
    def make_payment(cls, file, amount):
        '''

        :param amount: number - either 20000 or 10000
        :return: Boolean - True if payment is accepted, False otherwise
        '''
        user_d = ''
        with open(file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            # print(csv_reader)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                user_d = row

        if amount == 20000:
            user_d['Remaining Installment'] = 0
            user_d['Due Payment'] = 0

            with open(file, mode='w', newline='') as students_file:
                fieldnames = [
                    "Student's Name",
                    "Student's Email",
                    'Enroll On',
                    'Enrolled Course',
                    'Due Payment',
                    'Remaining Installment',
                    'Assessment Status',
                    'Course Status'
                ]
                student_writer = csv.DictWriter(students_file, fieldnames=fieldnames, dialect='excel')

                student_writer.writeheader()
                student_writer.writerow(user_d)
            return True

        elif amount == 10000:
            if user_d['Remaining Installment'] == 1 or user_d['Remaining Installment'] == 2:
                user_d['Due Payment'] -= 10000
                user_d['Remaining Installment'] -= 1

                with open(file, mode='w', newline='') as students_file:
                    fieldnames = [
                        "Student's Name",
                        "Student's Email",
                        'Enroll On',
                        'Enrolled Course',
                        'Due Payment',
                        'Remaining Installment',
                        'Assessment Status',
                        'Course Status'
                    ]
                    student_writer = csv.DictWriter(students_file, fieldnames=fieldnames, dialect='excel')

                    student_writer.writeheader()
                    student_writer.writerow(user_d)
                return True
            return False
        return False

    @classmethod
    def take_assessment(cls, file, marks):
        '''
        A student is not eligible to take assessment until he/she has due payment

        :param marks: number - total marked obtained by the student in the evaluation exam
        :return: Boolean - True if student passes, False otherwise
        '''
        user_d = ''
        with open(file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            # print(csv_reader)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                user_d = row
        # print(user_d)
        if user_d['Due Payment'] in [0, '0'] and marks >= cls.pass_marks:
            user_d['Assessment Status'] = 'pass'
            user_d['Course Status'] = 'completed'
            with open(file, mode='w', newline='') as students_file:
                fieldnames = [
                    "Student's Name",
                    "Student's Email",
                    'Enroll On',
                    'Enrolled Course',
                    'Due Payment',
                    'Remaining Installment',
                    'Assessment Status',
                    'Course Status'
                ]
                student_writer = csv.DictWriter(students_file, fieldnames=fieldnames, dialect='excel')

                student_writer.writeheader()
                student_writer.writerow(user_d)
            return True

        elif user_d['Due Payment'] in [0, '0'] and marks < cls.pass_marks:
            user_d['Assessment Status'] = 'fail'
            with open(file, mode='w', newline='') as students_file:
                fieldnames = [
                    "Student's Name",
                    "Student's Email",
                    'Enroll On',
                    'Enrolled Course',
                    'Due Payment',
                    'Remaining Installment',
                    'Assessment Status',
                    'Course Status'
                ]
                student_writer = csv.DictWriter(students_file, fieldnames=fieldnames, dialect='excel')

                student_writer.writeheader()
                student_writer.writerow(user_d)
            return True
        return False

    @classmethod
    def update_name(cls, file, new_name):
        user_d = ''
        with open(file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            # print(csv_reader)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                user_d = row
        # print(user_d)
        if user_d["Student's Name"]:
            user_d["Student's Name"] = new_name
            with open(file, mode='w', newline='') as students_file:
                fieldnames = [
                    "Student's Name",
                    "Student's Email",
                    'Enroll On',
                    'Enrolled Course',
                    'Due Payment',
                    'Remaining Installment',
                    'Assessment Status',
                    'Course Status'
                ]
                student_writer = csv.DictWriter(students_file, fieldnames=fieldnames, dialect='excel')

                student_writer.writeheader()
                student_writer.writerow(user_d)
            return True
        return False

    @classmethod
    def remove_user(cls, file):
        try:
            os.remove(file)
            return True
        except FileNotFoundError:
            return False


if __name__ == '__main__':
    s1 = Student(
        student_name='Gaurav Jaiswal',
        email = 'jr.gaurav2015@gmail.com',
        course = 'iOS Development',
        joining_date = datetime.date.today()
    )
    print(s1.check_student_status('registrations/jrgaurav2015gmailcom.csv'))
