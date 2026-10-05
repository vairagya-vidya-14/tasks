#if-else task
# 1.check given number is a 3-digit number or not 
n=int(input("enter a number"))
if(100<=n<=999):
    print("given number is 3-digit number")
else:
    print("given number is not a 3-digit number")

#2.Check whether a given number is divisible by both 3 and 5 or not.
n=int(input("Enter a number:"))
if(n%3==0 and n%5==0):
    print("Given number is divisible by 3 and 5")
else:
    print("given number is not  divisible by 3 and 5 ")
#3.Check whether a given triangle is a valid triangle or not.
     #hint :The sum of any two sides should be greater than the third side.
a=int(input("Enter first side:"))
b=int(input("Enter second side:"))
c=int(input("Enter third side:"))
if(a+b>c or b+c>a or c+a>b):
    print("given triangle is valid triangle ")
else:
    print("given triangle is not a valid triangle")

#4.Check whether a given number is a multiple of 10 or not.
n=int(input("enter the number:"))
if(n%10==0):
    print("Multiple of 10")
else:
    print("not a multiple of 10")


#if-elif-else -task
#1.Check the type of triangle based on its sides.
       # Equilateral, Isosceles, or Scalene.
a=int(input("Enter first side:"))
b=int(input("Enter second side:"))
c=int(input("Enter third side:"))
if(a==b==c):
    print("Equilateral triangle")
elif(a==b!=c or b==c!=a or c==a!=b):
    print("Isosceles triangle")
else:
    print("Scalene triangle")

#2.Calculate the electricity bill based on units consumed.
   # 0–100: ₹2/unit, 101–200: ₹3/unit, 201–300: ₹5/unit, above 300: ₹7/unit.
units=int(input("Enter electrcity bill :"))
if (units<100):
    print("total bill : ₹" ,units*2)
elif(units>=101 and units<=200):
    print("total bill : ₹",units*3)
elif(units>=201 and units<=300):
    print("total bill :₹" ,units*5)
else:
    print("total bill :₹",units*7)

#3.Display the age category.
   # Below 13 → Child, 13–19 → Teenager, 20–59 → Adult, 60 and above → Senior Citizen.
age=int(input("Enter the age:"))
if(age<13):
    print("Child")
elif(13<=age<=19):
    print("Teenager")
elif(20<=age<=59):
    print("Adult")
else:
    print("Senior Citizen")

#4.Calculate the discount based on shopping amount.
    #Below ₹1,000 → No discount, ₹1,000–₹4,999 → 10%, ₹5,000–₹9,999 → 20%, ₹10,000 and above → 30%.
amount=int(input("enter the amount:"))
if(amount<1000):
    print("No discount")
elif(1000<=amount<=4999):
    print("discount=10%")
elif(5000<=amount<=9999):
    print("discount=20%")
else:
    print("discount=30%")

#5.Display the season based on the month number.
  #  3–5 → Spring, 6–8 → Summer, 9–11 → Autumn, 12/1/2 → Winter.
month_num=int(input("Enter the month number:"))
if(3<=month_num<=5):
    print("Spring")
elif(6<=month_num<=8):
    print("Summer")
elif(9<=month_num<=11):
    print("Autuman")
else:
    print("Winter")

#6.Check whether a given year is a Leap Year or not.
    # Condition 1: year % 400 == 0
    # Condition 2: year % 4 == 0 and year % 100 != 0
y=int(input("Enter Year :"))
if(y%400==0):
    print("Leap Year")
elif(y%4==0 and y%100!=0):
    print("Leap Year")
else:
    print("Not a leap year")

#Nested if – Tasks
#1.Check whether a person is eligible to donate blood.
    #Age should be between 18 and 60. If eligible by age, weight should be above 50 kg.
age=int(input("Enter the age:"))
if(18<=age<=60):
    weight=int(input("Enter the weight:"))
    if(weight>50):
        print("eligible to donate blood")
    else:
        print("not eligible")
else:
    print("not eligible")

#2.Display the grade based on average only if the student has passed in all 4 subjects.
a=int(input("Enter the marks in maths:"))
b=int(input("enter the marks in science:"))
c=int(input("Enter the marks in social:"))
d=int(input("Enter the marks in english:"))
if(a>=35 and b>=35 and c>=35 and d>=35):
    avg=(a+b+c+d)/4
    if(avg>90):
        print("Grade= s")
    elif(81<=avg<=90):
        print("Grade=A")
    elif(71<=avg<=80):
        print("Grade=B")
    elif(61<=avg<=70):
        print("Grade=C")
    elif(51<=avg<=60):
        print("Grade=D")
    elif(41<=avg<=50):
        print("Grade=E")
    else:
        print("Fail")
else:
    print("Fail")

#.Check whether a student is eligible for a scholarship.
    #Age should be above 18. If eligible by age, score should be above 86.
age=int(input("Enter the age of student:"))
if(age>18):
    score=int(input("Enter the score:"))
    if(score>86):
        print("Eligible for a scholarship.")
    else:
        print("Not eligible")
else:
    print("Not Eligible")
