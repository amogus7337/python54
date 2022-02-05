sum = int (input('sum'))
if 500 <= sum <= 1000:
    s = sum * 0.03
else:
    s = sum * 0.05
sum -= s
print(sum)
