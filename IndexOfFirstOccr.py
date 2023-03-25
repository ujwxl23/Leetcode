haystack="hello"
needle="ll"

hl,nl= len(haystack),len(needle)
if hl==0 or nl==0:
    print (-1)
if nl>hl:
    print (-1)
for i in range(0,hl-nl+1):
    haystack1 = haystack[i:i+nl]
    if haystack1==needle:
        print (i)
    else:
        print (-1)