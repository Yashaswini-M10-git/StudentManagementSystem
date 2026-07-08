class Student:
    def __init__(self,roll,name):
        self.roll=roll
        self.name=name
    def information_student(self):
        print(f"Student roll:{self.roll}  | Student name:{self.name}")
class StudentManagementSystem:
    def __init__(self):
        self.students=[]
    def add_student(self,student):
        self.students.append(student)
    def display_student(self):
        if not self.students:
            print("No Students Found")
            return
        for student in self.students:
            student.information_student()
    def search_student(self,roll):
        for student in self.students:
            if student.roll==roll:
                print("Student found")
                student.information_student()
                return
        print("No Student Found")
    def update_student(self,roll,name):
        for student in self.students:
            if student.roll==roll:
                self.name=name
                print(f"New student roll:{roll} |New student name:{name}")
                return
        print("No Student Found")
    
    def delete_student(self,roll):
        for student in self.students:
            if student.roll==roll:
                self.students.remove(student)
                print(f"Student roll:{student.roll} | Student name:{student.name} has been removed")
                return
        print("No Studnet Found")


student1=Student(1,"Yashaswini M")
student2=Student(2,"Yukta")
student3=Student(3,"Yamini")
student4=Student(4,"Zara")

sms1=StudentManagementSystem()
sms1.add_student(student1)
sms1.add_student(student2)
sms1.add_student(student3)
sms1.add_student(student4)

sms1.display_student()
sms1.search_student(1)
sms1.update_student(3,"Meghana")
sms1.delete_student(4)


