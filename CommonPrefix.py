strs=["flower","flow","flight"]
for i in range(len(strs)):
            if strs[i] =='':
                print("")
if (len(strs)==1):
    print(strs[0])
elif (len(strs)>=2):
    l1=strs[0]
    l2=strs[1]
if (len(l1)>=len(l2)):
    m=len(strs[1])
else:
    m=len(strs[0])
l=[]
st1=""
if l1[0]==l2[0]:
    l.append(0)
    st=""
    for k in l:
        st=st+l1[k]
    lf=[w for w in strs if w.startswith(st)]
    if (len(strs)==len(lf)):
        st1=st
    for j in range(1,m):
        if l1[j]==l2[j]:
            l.append(j)
            st=""
            for k in l:
                st=st+l1[k]
            lf=[w for w in strs if w.startswith(st)]
            if (len(strs)==len(lf)):
                st1=st
        else:
            break
    print(st1)
else:
    print("There is no common prefix among the input strings.")