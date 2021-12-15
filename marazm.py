chislo = int (input ("угадай число"))
b = 9
while (chislo != b):
    if chislo>b:
        print ('меньше')
    elif chislo<b:
        print ('больше')
    else:
        print ('угадал')
    chislo = int (input ("введите число"))
print("число верное")