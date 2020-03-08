a=int(input()) #Enter of stars required at the last line
b=a//2
for i in range(1,a+1):
    if i%2!=0:
        print(" "*b,"*"*i," "*b)
        b=b-1 
