###1.single Inheritance with poliymorphism.
class BankAccount:
    def Interest(self):
        print("Bank Account Interest")
class SavingsAccount(BankAccount):
    def Interest(self):
        print("Savings account gets 6 per interest")

s=SavingsAccount()
s.Interest()

b=BankAccount()
b.Interest()

##2.single Inheritance with poliymorphism.

class Payment:
    def pay(self):
        print("Making Payments")
class UPI(Payment):
    def pay(self):
        print("Payment made using UPI")

p=Payment()


u=UPI()
u.pay()

#__________________________________________________________________________________________________________________________#

##3.multilevel Inheritance Using polymorphism.

class School:
    def details(self):
        print("School Name: ABC School")
        print("Location: Hyderabad")


class Student(School):
    def details(self):
        print("Student Name: Rahul")
        print("Student ID: 101")
        print("Course: Computer Science")


class GraduateStudent(Student):
    def details(self):
        print("Specialization: Data Science")
        print("Graduation Year: 2026")


s = School()
st = Student()
g = GraduateStudent()

s.details()

st.details()

g.details()


##4.multilevel Inheritance Using polymorphism.
class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def work(self):
        print("Developer is writing code")


class SeniorDeveloper(Developer):
    def work(self):
        print("Senior Developer is designing the application")


e = Employee()
d = Developer()
sd = SeniorDeveloper()

e.work()

d.work()

sd.work()

#______________________________________________________________________________________________________________________#

##5.multiple Inheritance Using polymorphism.

class Printer:
    def operate(self):
        print("Printer is printing a document")


class Scanner:
    def operate(self):
        print("Scanner is scanning a document")


class AllInOneMachine(Printer, Scanner):
    def operate(self):
        print("All-in-one machine is printing and scanning")


p = Printer()
s = Scanner()
a = AllInOneMachine()

p.operate()
print()

s.operate()
print()

a.operate()

##6.multiple Inheritance Using polymorphism.
class Teacher:
    def work(self):
        print("Teacher is teaching students")


class Researcher:
    def work(self):
        print("Researcher is conducting research")


class Professor(Teacher, Researcher):
    def work(self):
        print("Professor is teaching and conducting research")


t = Teacher()
r = Researcher()
p = Professor()

t.work()
print()

r.work()
print()

p.work()

#_________________________________________________________________________________________________________________________#

###7.hierachical inheritance with polymorphism.
class Shape:
    def area(self):
        print("Calculating area")


class Circle(Shape):
    def area(self):
        print("Area of Circle = π X r X r")


class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle = length X width")


s = Shape()
c = Circle()
r = Rectangle()

s.area()
c.area()
r.area()


###8.hierachical inheritance with polymorphism.

class Payment:
    def pay(self):
        print("Making a payment")


class CreditCard(Payment):
    def pay(self):
        print("Payment made using Credit Card")


class UPI(Payment):
    def pay(self):
        print("Payment made using UPI")


p = Payment()
c = CreditCard()
u = UPI()

p.pay()
c.pay()
u.pay()
