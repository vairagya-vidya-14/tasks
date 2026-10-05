# 1. # Sum of Prime Numbers
# # Find the sum of all prime numbers between 20 and 150.
sum=0
print(f"Prime numbers in range 20 to 150 are :")
for j in range(21,150,1):
    n=j
    count=0
    for i in range(1,n+1,1):
        if(n%i==0):
            count+=1
    if count==2:
        sum += n
print(sum)

# 2. # Average of Perfect Numbers
# # Find the average of all perfect numbers between 1 and 1000.
res=0
count=0
print("Average of Perfect Numbers between 1 and 1000 are :")
for j in range(2,1000,1):
    sum=0
    n=j
    for i in range(1,n,1):
        if(n%i==0):
            sum+=i       
    if sum==n:
        res+=n
        count+=1
print(f"Average={res/count}")
            
# 3. # Leap Years in a Range(Not Nested Loop Logic)
# # Print all leap years between 1900 and 2026.
print("Leap Years in range 1900 to 2026 are :")
for year in range(1901,2026,1):
    if(year%400==0 or( year%4==0 and year%100!=0) and year%100!=0):
        print(year,end="  ")
    
# 4. # Palindrome Numbers
# # Print all palindrome numbers between 100 and 500.
print("Palindrome numbers in between 1001 and 500 are :")
for j in range(101,500,1):
    n=j
    temp=n
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if temp==rev:
        print(rev,end="  ")
    
# 5. # Digit Sum = 10
# # Print all numbers between 120 and 850 whose digit sum is exactly 10.
print("Numbers digit sum is 10 are :")
for j in range(121,850,1):
    n=j
    sum=0
    for i in range(1,n+1,1):
        r=n%10
        n=n//10
        sum=sum+r
    if(sum==10):
        print(i,end="  ")
    
    
# 6. # Pairs with Target Sum
# # Print all pairs (a, b) between 1 and 50 whose sum is 30. Print each pair only once.
for i in range(2,50,1):
    for j in range(1,51,1):
        if(i+j==30 and i<=j):
            print(f"a = {i} b = {j}")
    
# 7. # Exactly 3 Factors
# # Print all numbers between 10 and 300 that have exactly 3 factors.
print("Factors between 10 and 300 that have exactly 3 factors are :")
for j in range(11,300,1):
    n=j
    count=0
    for i in range(1,n+1,1):
        if(n%i==0):
            count=count+1
    if(count==3):
        print(n,end="  ")

# 8. # Prime Factors
# # Print the prime factors of every number between 20 and 50.
for k in range(21,50,1):
    n=k
    print(f"prime factors of {k} = ",end=" ")
    for i in range(1,n+1,1):
        if(n%i==0):
            count=0
            for j in range(1,i+1,1):
                if i%j==0:
                    count+=1
            if count==2:
                print(i,end=" ")
    print()
        
# 9. # Armstrong Numbers
# # Print all Armstrong numbers between 100 and 999.
for j in range(101,999,1):
    n=j
    temp=n
    digit=0
    sum=0
    while n>0:
        r=n%10
        sum=sum+r**3
        n=n//10
    if temp==sum:
        print(sum)

10. # Maximum Factors
# Find the number between 50 and 150 that has the maximum number of factors.
max_count=0
max_num=0
for j in range(51,150,1):
    count=0
    n=j
    for i in range(1,n+1,1):
        if(n%i==0):
            count+=1
        if count>max_count:
            max_count=count
            max_num=j
print(f"Maximum number = {max_num}")
print(f"Maximum factors = {max_count}")
print(f"Factor of {max_num} = ",end=" ")
for i in range(1,max_num+1,1):
    if max_num%i==0:
        print(i,end=" ")