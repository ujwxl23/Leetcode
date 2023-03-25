st="(]"
s=0
if (len(st)%2==0):
    for i in range(0,len(st)-1):
        if (st[i]=="("):
            if (st[i+1]==")"):
                s=1
            else:
                s=0
        elif (st[i]=="{"):
            if (st[i+1]=="}"):
                s=1
            else:
                s=0
        elif (st[i]=="["):
            if (st[i+1]=="]"):
                s=1
            else:
                s=0
if (s==1):
    print("true")
else:
    print("false")