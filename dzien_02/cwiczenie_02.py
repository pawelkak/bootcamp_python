suma_liczb = 0
ilosc_zapytan = 0

while True:
    dane = input("Podaj lub K")

    if dane == "k":
        break

    dane = int(dane)
    suma_liczb = suma_liczb + dane
    ilosc_zapytan += 1

print("srednia wynosi", suma_liczb / ilosc_zapytan)