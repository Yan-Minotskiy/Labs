Stone = int(input())
while Stone > 0:
    if Stone > 6 or Stone == 3:
        Stone -= 3
        print(Stone, 3)
    elif Stone == 6 or Stone == 2:
        Stone -= 2
        print(Stone, 2)
    elif Stone == 5 or Stone == 1:
        Stone -= 1
        print(Stone, 1)
    else:
        Stone -= 1
        print("Вы выиграли")
        break
    if Stone != 0:
        Stone -= int(input())
    else:
        print("ИИ выиграл")