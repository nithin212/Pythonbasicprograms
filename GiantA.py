"""Write a program that prints a giant letter A """
n=int(input())
m=math.ceil(n/2)
a=m
b=m
for i in range(1,m+1):
    for k in range(1,n+1):
        if(i==math.ceil(m/2)):
            if(k>=a and k<=b):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        else:
            if(k==a or k==b):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    a=a-1
    b=b+1
    print()
