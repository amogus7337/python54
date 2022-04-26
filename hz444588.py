import random


k= input('Ввидите каманду')
if k == 'D':
    spisok.append(k)
    print(spisok)
    for stroka in range(len(spisok)):
        for stolb in range(len(spisok)):
            if spisok[stroka][stolb] == "o" :
                a = stroka
                g = stolb
    spisok[a][g]='*'
    spisok[a-1]
           
spisok =[['о', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]

for stroka in spisok:
    for stolb in stroka:
        print(stolb, end="")
    print()
    
r = int (input('какой номер строки ?'))
s = int (input('какая цифра столбца ?'))

if r<0 or r>10 :
    r = int (input('какой номер строки ?'))

    if g<0 or g>10 :
        s = int (input('какая цифра столбца ?'))

a = 0
g = 0
for stroka in range(len(spisok)):
    for stolb in range(len(spisok)):
        if spisok[stroka][stolb] == "o" :
            a = stroka
            g = stolb
spisok[a][g]='*'
spisok[r][s]='o'
for stroka in spisok:
    for stolb in stroka:
        print(stolb, end="")
    print()