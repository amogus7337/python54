import random


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

for stroka in spisok:
    for stolb in stroka:
        if spisok == "o" :
            a = stroka
            g = stolb
spisok[a][g]='*'

         

