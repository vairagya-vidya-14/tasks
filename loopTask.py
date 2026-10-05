#1.find the average of numbers from 1 to n.
# n=int(input("enter the number"))
# sum=0
# for i in range(1,n+1,1):
#     sum=sum+i
# avg=sum/n
# print(f"the average of  {n} numbers is {avg}")

#2.find the sum of squares of numbers from 1 to n
# n=int(input("enter a number"))
# sum=0
# for i in range(1,n+1,1):
#     sq=i*i
#     sum=sum+sq
# print(f"sum of  squares of 1 to {n} is {sum}")

#3.find the sum of cubes of numbers from 1 to n
# n=int(input("enter a number"))
# sum=0
# for i in range(1,n+1,1):
#     cube=i*i*i
#     sum=sum+cube
# print(f"the sum of  cubes of 1 to {n} is {sum} ")

#4.calculate the power of a number without using the ** operator
base=int(input("enter a base number"))
power=int(input("enter a power number"))
for i in range(1,power+1,1):
    base=base*i
print(base)

#5 display the first n terms of the fibanacci series.
# n=int(input("enter the number"))
# a=0
# b=1
# print(a)
# print(b)
# for i in range(1,n-1,1):
#     c=a+b
#     a=b
#     b=c
#     print(c)

#6 display the first n terms of the series
# n=int(input("enter a number"))
# print(1)
# for i in range(2,n+1,1):
#     print(f"1/{i}")


#7 display the first n terms of the series

# n=int(input("enter the number of terms"))
# num=1
# for i in range(1,n+1,1):
#     print(num)
#     num=num+(10**i)

#8 display the first n terms of the series

# n=int(input("enter a number"))
# print(1)
# num=1
# for i in range(1,n+1,1):
#     num=num*3
#     print(num)