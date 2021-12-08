login  = input ("введите login")
num = input ("введите пароль")
while(login != "Admin"or num != "445588"):
    if login ==  "Admin":
      print(" логин верный,пароль не верный ")
    if num == "445588":
      print(" пароль верный,логин не верный ")
    if login != "Admin" and num != "445588":
      print( "пароль и логин не верный" )
    login  = input ("введите login")
    num = input ("введите пароль")
print("доброго дня ")
    