lstnumeri = []
quantinumeri = int(input("Inserisci la quanti di numeri da aggiungere: "))
for i in range(quantinumeri):
    numero = int(input("Inserisci numeri: "))
    lstnumeri.append(numero)


lstnumeri.sort(reverse = True)

print(lstnumeri)
