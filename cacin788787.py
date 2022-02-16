SPISOK =[]
a= input('Ввидите каманду')
if a =='добавить':
    b = input("Ввидите элемент")
    SPISOK.append(b)
    print(SPISOK)
elif 'удалить':
    b = input("Ввидите элемент")
    SPISOK.remove(b)
    print(SPISOK)
