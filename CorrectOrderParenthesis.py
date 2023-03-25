s="[]"
st=0
if (len(s)%2==0):
    for i in range(0,len(s)-1):
        if (s[i]=="("):
            if (s[i+1]==")"):
                st=1
            else:
                st=0
        elif (s[i]=="{"):
            if (s[i+1]=="}"):
                st=1
            else:
                st=0
        elif (s[i]=="["):
            if (s[i+1]=="]"):
                st=1
            else:
                st=0
if (st==1):
    print("true")
elif (st==0):
    print("false")