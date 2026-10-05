# 1.Find the sum of digits in a given number.
#     Example: 738 → 7 + 3 + 8 = 18
# n=738
# sum=0
# while(n!=0):
#     ld=n%10
#     sum=sum+ld
#     n=n//10
# print(sum)

# 2.Find the average of digits in a given number.
#      Example: 624 → (6 + 2 + 4) / 3 = 4

# n=624
# count=0
# sum=0
# avg=0
# while(n!=0):
#     ld=n%10
#     count=count+1
#     sum=sum+ld
#     n=n//10
# print(f"avg={sum/count}")

#3.Find the sum of the first digit and the last digit of a given number.
    #  Example: 936 → 9 + 6 = 15
# n=936
# sum=0
# last=n%10
# print(last)
# while(n!=0):
#     ld=n%10
#     n=n//10
# print(ld)
# sum=last+ld
# print(sum)

# 4.Find the average of digits that are divisible by 5 in a given number.
#      Example: 12575 → Divisible by 5 digits: 5, 5, 
# n=12575
# count=0
# sum=0
# while(n!=0):
#     ld=n%10
#     if(ld%5==0):
#         count=count+1
#         sum=sum+ld
#     n=n//10
# print(f" avg={sum/count}")

#5.Find the difference between the largest digit and the smallest digit in a given number.
    #  Example: 58321 → Largest = 8, Smallest = 1 → Difference = 8 - 1 = 7

# n=78902
# l=0
# s=n
# while(n!=0):
#     ld=n%10
    
#     if(ld>l):
#         l=ld
#     if(ld<s):
#         s=ld
#     n=n//10
# print(f" difference={l}-{s} ={l-s}")