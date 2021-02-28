st1 = int(input("Сколько камней в 1 куче? "))
st2 = int(input("Сколько камней во 2 куче? "))
st3 = int(input("Сколько камней в 3 куче? "))
nim = st1 ^ st2 ^ st3
if nim > 0:
    if st1 ^ nim < st1:
        dif = st1 - (st1 ^ nim)
        st1 -= dif
        get = st1
        num = 1
    elif st2 ^ nim < st2:
        dif = st2 - (st2 ^ nim)
        st2 -= dif
        get = st2
        num = 2
    else:
        dif = st3 - (st3 ^ nim)
        st3 -= dif
        get = st3
        num = 3
else:
    st1 -= 1
    dif = 1
    num = 1
    get = st1
print("Я забрал " + str(dif) + " камней из " + str(num) + " кучи, теперь там " + str(get) + " камней. Твой ход")
while st1 + st2 + st3 > 0:
    step = 2
    num = 0
    while num < 1 or num > 3:
        num = int(input("Из какой кучи? "))
        if num == 1 and st1 == 0 or num == 2 and st2 == 0 or num == 3 and st3 == 0:
            print("Здесь уже нет камней!")
            num = 0
    con = True
    while con:
        if num == 1:
            get = st1
        elif num == 2:
            get = st2
        else:
            get = st3
        dif = int(input("Сколько (но не больше " + str(get) + ")?"))
        if dif > 0 and dif <= get:
            if num == 1:
                st1 -= dif
                get = st1
            elif num == 2:
                st2 -= dif
                get = st2
            else:
                st3 -= dif
                get = st3
            print("Ты забрал " + str(dif) + " камней из " + str(num) + " кучи, теперь там " + str(
                get) + " камней. Мой ход")
            con = False
    if st1 + st2 + st3 > 0:
        step = 1
        nim = st1 ^ st2 ^ st3
        if nim > 0:
            if st1 ^ nim < st1:
                dif = st1 - (st1 ^ nim)
                st1 -= dif
                get = st1
                num = 1
            elif st2 ^ nim < st2:
                dif = st2 - (st2 ^ nim)
                st2 -= dif
                get = st2
                num = 2
            else:
                dif = st3 - (st3 ^ nim)
                st3 -= dif
                get = st3
                num = 3
        else:
            if st1 > 0:
                st1 -= 1
                num = 1
                get = st1
            elif st2 > 0:
                st2 -= 1
                num = 2
                get = st2
            else:
                st3 -= 1
                num = 3
                get = st3
            dif = 1
        print("Я забрал " + str(dif) + " камней из " + str(num) + " кучи, теперь там " + str(get) + " камней. Твой ход")
if step == 1:
    print("Я победил")
else:
    print("Ты победил")
