try:
    a = int(input("1-son: "))
    amal = input("Amalni kiriting: ")
    b = int(input("2-son: "))
    c = 0

    if amal == "+":
        print("yigindi", str(a+b), "ga teng")
        while c < (a+b):
            c += 1
            print(c)
    elif amal == "-":
        print("ayirma", str(a-b), "ga teng")
        while c < (a-b):
            c += 1
            print(c)
    elif amal == "*":
        print("kopaytma", str(a*b), "ga teng")
        while c < (a*b):
            c += 1
            print(c)
    elif amal == "/":
        print("bulinma", str(a/b), "ga teng")
        while c < (a/b):
            c += 1
            print(c)
    else:
        print("Xatolik notogri amal kiritdingiz")
except ZeroDivisionError:
    print("0ga bo'lib bo'lmaydi")
except ValueError:
    print("Xato qiymat kiritdingiz. Son kiriting")
except:
    print("Sizda qandaydir xatolik bor")
