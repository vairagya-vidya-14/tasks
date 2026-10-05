# Find the first even digit from the left in 753914286.
# n=753914286
# num=n

# while(n!=0):
#     ld=n%10
#     if(ld%2==0):
#         temp=ld
#     n=n//10
# print(temp)

# Find the first prime number between 50 and 100.
# for i in range(50,101,1):
#     n=i
#     count=0
#     for j in range(1,n+1,1):
#         if(n%j==0):
#             count=count+1
#     if(count==2):
#         print(n)
#         break

#Find the first number whose digit sum is 10.
# for i in range(10,50,1):
#     count=0
#     n=i
#     num=n
#     sum=0
#     while(n!=0):
#         ld=n%10
#         sum=ld
#         n=n//10
#         sum=sum+n
#         if(sum==10):
#             count=count+1
#             print(num)
#             break
#     if(count==1):
#         break
    
# Find the first number with exactly 3 divisors between 1 and 100.
# count=0
# for i in range(1,100,1):
#     for j in range(1,i-1,1):
#         if(i%j==0):
#             count=count+1
#             if(count==3):
#                 print(i)
#                 break

# Stop when 3 consecutive odd numbers occur between 1 and 50.
# count=0
# for i in range(1,100,1):
#     if(i%2!=0):
#         count=count+1
        
#         if(count==3):
#             print("stoped at ",i)
#             break

# Find the first palindrome between 10 and 500.
# for i in range(10,50,1):
#     n=i
#     num=n
#     rev=0
#     while(n!=0):
#         ld=n%10
#         rev=rev*10+ld
#         n=n//10
#     if(rev==num):
#         print(num)
#         break

# Find the first perfect number between 1 and 1000.
# for i in range(1,1000,1):
#     sum=0
#     n=i
#     for j in range(1,n,1):
#         if(n%j==0):
#             sum=sum+j
#     if(sum==n):
#         print(n)
#         break

# Print the first 5 even numbers.
# count=0
# for i in range(1,50,1):
#     if(i%2==0):
#         print(i)
#         count=count+1
#         if(count==5):
#             break

# Print the first 5 prime numbers.

# countp=0
# for i in range(1,50,1):
#     n=i
#     count=0
    
#     for j in range(1,n+1,1):
#         if(n%j==0):
#             count=count+1

#     if(count==2):
#         countp=countp+1
#         print(n)
        
#         if(countp==5):
#             break
    

# Print the first 3 numbers divisible by 7.
# count=0
# for i in range(1,50,1):
#     if(i%7==0):
#         print(i)
#         count=count+1
#     if(count==3):
#         break