def NFibonacciTerm(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return NFibonacciTerm(n-1)+NFibonacciTerm(n-2)
a=int(input())
if(a>0):
    print(NFibonacciTerm(a))

