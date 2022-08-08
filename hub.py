

print("1-per cancellare la lista/n "
      "2-per stamparla"
      "3-sostituirla")

x = int(input('inserire il codice'))
if x == 1:
    lstnumeri.clear()
    print(lstnumeri)
if x == 2:
    print(lstnumeri)
if x == 3:
    lstnumeri.clear()
    quantinumeri = int(input("Inserisci la quanti di numeri da aggiungere: "))
    for i in range(quantinumeri):
        numero = int(input("Inserisci numeri: "))
        lstnumeri.append(numero)
    lstnumeri.sort(reverse=True)

    print(lstnumeri)


