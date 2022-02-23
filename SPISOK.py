SPISOK =['incredibox','poppy playtimv','fnaf +','Fall Guys: Ultimate Knockout']
while True:
    a = input('Ввидите каманду')
    if a =='добавить':
        b = input("Ввидите элемент")
        SPISOK.append(b)
        print(SPISOK)
    elif a =='удалить':
        b = input("Ввидите элемент")
        SPISOK.remove(b)
        print(SPISOK)
    elif a =='редакт':
        s = int (input("какой элемент заменить"))#идекс элемента в списке
        g = input("Ввидите новыий  элемент")
        SPISOK[s]=g
        print(SPISOK)
    else:
        print('каманда не верна:/')
