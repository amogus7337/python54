import random

slava = ["ученый", "пк", "дом", "мод", "игра", "одежда",]

word=slava[random.randrange(5)]
len_slava=len(slava)
health = 10
test=False
used_slava= " "
vin_slava=[]
# заполнение массива для слова в игре
for s in range(len(slava)):
    win_slava+="_"
    
while len_slava != 0 and health != 0:
    test = False
    #ввод буквы и проверка на повтор
    while True:
        letter = input("\nвведите букву ")
        if letter in used_letters or len(letter)>1:
            print ("\nНе больше одного символа, попробуйте снова!")
        else:
            used_letter
            break
        
        count=0
        for s in slava:
            if letter in s :
                len_slava -= 1
                test=True
                win_slava[count]=letter
                count+=1
                
                if not test:
                    health -= 1
                    print ("НЕВЕРНО")
                else:
                    print("ВЕРНО")
                    print(win_slava)
                    
                print("ваше здоровье = ", health)
                
            if(len_slava == 0):
                print("nПОБЕДИТЕЛЬ!!! Слово было", word.upper())
            else:
                print("\nВЫ ПРОИГРАЛИ! ПОПРОБУЙТЕ СНОВА!")


