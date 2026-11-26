while True:
    print("Hesablamaq üçün seçin:+,-,*,/ (Çıxış:q)")
    A=input("seçiminizi qeyd ddin: ")
    if A == "q":
        break
    elif A == "+":
        try:
            B=int(input("Bir rəqəm seçin: "))
            C=int(input("Bir rəqəm seçin: "))
            print(B+C)
        except ValueError:
            print("Yanliz rəqəm seçin!")
    elif A == "-":
        try:
            B=int(input("Bir rəqəm seçin: "))
            C=int(input("Bir rəqəm seçin: "))
            print(B-C)
        except ValueError:
            print("Yanliz rəqəm daxil edin!")
    elif A == "*":
        try:
            B=int(input("Bir rəqəm seçin: "))
            C=int(input("Bir rəqəm seçin: "))
            print(B*C)
        except ValueError:
            print("Yanliz rəqəm seçin: ")
    elif A == "/":
        try:
            B=int(input("Bir rəqəm seçin: "))
            C=int(input("Bir rəqəm seçin: "))
            print(B/C)
        except ValueError:
            print("Yanliz rəqəm daxil edin!")
        except ZeroDivisionError:
            print("(0) Bölmek mümkün deyil!")
    else:
        print("Zəhmət olmasa sadece yazilan işarelerden birirni seçin")

