stra="Hi how are you"
newstr=""
for k,j in enumerate(stra):
    if(k %2!=0):
        newstr=newstr+"42"
    else:
        newstr=newstr+stra[k]
