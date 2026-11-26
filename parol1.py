while True:
     parol=input("parol yaz (cixmaq ucun q) :")
     if parol == "q":
         break
     elif len(parol) <= 6:
         print("Zeifdir")
     elif len(parol) <= 10:
         print("Orta derece")
     else:
         print("Güclüdür")
     if any(c.isdigit() for c in parol):
         print("parolda reqem var")

