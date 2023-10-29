name = int ( input("Введите кол-во рублей"))
if name%10==1 and name%100!=11:
    print(name, "рубль")
elif 2<= name% 10<=4 and (name % 100<10 or name%100>=20):
    print(name , "рубля")
else:
    print(name , "рублей")

