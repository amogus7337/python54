sum = int (input('sum'))
s = 0 
if  sum <= 1000:
    s = sum * 0
elif sum >  1000  and sum<= 5000:
    s = sum * 0.05
elif sum >  5000  and sum<=10000:
    s = sum * 0.10
elif sum > 10000:
    s = sum * 0.15
sum -= s
print(sum)