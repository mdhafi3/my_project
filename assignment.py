class course:
    def __init__(self,course_name):
        self.course_name = course_name

class Studentdata:
    def __init__(self,Student_name,Roll_no,Authonication_key):
        self.Student_name = Student_name
        self.Roll_no = Roll_no
        self.__Authonication_key = Authonication_key
        self.course_name = []

    def enroll_class(self,course):
        self.course_name.append(course)

    def get_authnication_key(self):
        return self.__Authonication_key


def view_data():
    with open("students.txt","r") as line:
        for each_line in line:
            print(each_line)
while True:
    x = input("enter course Name: ")
    y = input("Enter name of Student: ")
    z = input("Enter Roll Number: ")
    p = input("Type Secrect code of your Dashboard: ")

    if len(x)<5:
        print("Enter valid Batch Name then try")
        continue
    elif len(y)<5:
        print("Enter valid Student Name then try")
        continue
    elif len(z)==0:
        print("Enter Valid Roll number of every sutdent")
        continue
    elif len(p)<6:
        print("Type Valid Security key like Capital Number, Smaller number, Number & Special key atleast 8digit and Unique. Remember it and dont share with others")
        continue
    else:
        print("Congratulations Your Registration Process has been successfully Completed. Now you can Registration next one by click Run code button and input data into Terminal interface")
        courses = course(x)
        data = Studentdata(y, z, p)
        print(data.course_name)
    with open("Students.txt", "a") as db_file:
        db_file.write(f"Name: {data.Student_name}, Roll No: {data.Roll_no},  Course Name: {x},  Password: {data.get_authnication_key()} \n")
    # view_data()
    break


