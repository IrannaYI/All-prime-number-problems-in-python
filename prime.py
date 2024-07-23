#n prime num
# # n=5
# c=0
# i=2

# while c!=n:
#     for j in range(2,i):
#         if i%j==0:
#             break
    
#     else:
#         c=c+1
#         print(i,",",c)
#     i=i+1

#nth prime num
# n=15
# c=0
# i=2

# while c<n:
#     for i in range(2,i):
#         if i%2==0:
#             break
    
#     else:
#         c=c+1
#         if c==n:
#             print(i)
    # i=i+1



#prime factors

# n=12

# for i in range(2,n+1):
#     if n%i==0:
#         for j in range(2,i):
#             if i %j==0:
#                 # print(j)
#                 break

#         else:
#             print(i)


#prime number m to n
# m=99
# n=101

# for i in range(m,n+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else: 
#         print(i)


#What is the sum of the first 20 prime numbers?
# m=1
# n=20
# sum=0
# for i in range(m,n):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         sum=sum+i
# print(sum)

#If “p” is the prime number, find the number of factors p3 has.
# p= int(input("enter"))

# for i in range(2,p):
#     if p%i==0:
#         break
# else:
#     print("not prime and its cube ",end="")
#     f=p**3
#     print(f)

# for j in range(1,f+1):
#     if f%j==0:
#         print(j)

