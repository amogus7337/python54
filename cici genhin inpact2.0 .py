n = int (input())
a = int (input())
c = int (input())
if a>n:
    if a>c:
        print(str(a)+"Больше")
    else:
        print(str(c)+"Больше")
else:
    if n>c:
        print(str(n)+"Больше")
    else:
        print(str(c)+"Больше")
