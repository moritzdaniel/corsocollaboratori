#Creation and Implementation
from contextlib import nullcontext
from test_ordinamento import *

print("abceddesdfsda")
lstnumeri = []
quantinumeri = int(input("Inserisci la quanti di numeri da aggiungere: "))
if test_num_array(quantinumeri)==False:
    for i in range(quantinumeri):
        numero = int(input("Inserisci numeri: "))
        lstnumeri.append(numero)
    lstnumeri.sort(reverse = True)
    if test_reverse(lstnumeri)==False:
        print(lstnumeri)