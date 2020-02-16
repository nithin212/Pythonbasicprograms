o=int(input()) #"Enter the number of levels of stars required
print("\n")
b=1
for i in range(1,o//2+1):
    l=o//2
    print(" "*l,"*"*b," "*l)
    o=o-2
    b=b+2
