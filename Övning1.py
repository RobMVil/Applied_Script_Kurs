num1 = 30
num2 = 30

if num1 < num2:
    print("num2 är större")
elif num2 < num1:
    print("num är större")
else:
    print("Lika stora")


num3 = None

if num3 == 10:
    print("Ej")
elif num3 == None:
    print("num3 är lika med None")
else:
    print("fail")


is_sunny = True
is_warm = False

if is_sunny == True and is_warm == True:
    print("Det är soligt och varmt")
elif is_sunny == True and is_warm == False:
    print("Det är soligt")
elif is_sunny == False and is_warm == True:
    print("Det är varmt")
else:
    print("Det är varken varmt eller soligt")

number = 5
print(number)
number +=3
print(number)

#Lägger till en kommentar