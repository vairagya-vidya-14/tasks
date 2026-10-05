# Print 1–30, skipping even numbers.
# for i in range(1,30,1):
#     if(i%2==0):
#         continue
#     print(i)

# Print 1–40, skipping multiples of 4.
# for i in range(1,40,1):
#     if(i%4==0):
        
#         continue
#     print(i)

# Print 1–30, skipping numbers from 10–20.
# for i in range(1,31,1):
#     if(i>10 and i<=20):
#         continue
#     print(i)

# Print 1–50, skipping multiples of 3.
# for i in range(1,50,1):
#     if(i%3==0):
#         continue
#     print(i)

# Extract 502304, skipping digit 0.
# n=502304
# while(n!=0):
#     ld=n%10
#     if(ld==0):
#         n=n//10
#         continue
#     print(ld)
#     n=n//10

# Extract 5832461, printing only even digits.
# n=5832461
# while(n!=0):
#     ld=n%10
#     if(ld%2!=0):
#         n=n//10
#         continue
#     print(ld)
#     n=n//10

# Extract 1432578, skipping odd digits.
# n=1432578
# while(n!=0):
#     ld=n%10
#     if(ld%2!=0):
#         n=n//10
#         continue
#     print(ld)
#     n=n//10

# Print 1–200, skipping multiples of 3 or 5.
# for i in range(1,200,1):
#     if(i%3==0 and i%5==0):
#         continue
#     print(i)


# Print 1–500, skipping numbers with odd digit sum
# for i in range(1,500,1):
#     n=i
#     sum=0
#     while(n!=0):
#         ld=n%10
#         sum=sum+ld
#         n=n//10
#     if(sum%2!=0):
#         continue
#     print(i)

# Print 1–500, skipping numbers containing digit 0.
# for i in range(1,500,1):
#     n=i
#     has_zero=False
#     while(n!=0):
#         ld=n%10
#         if(ld==0):
#             has_zero=True
#             break
#         n=n//10
#     if has_zero==False:
#         print(i)
        