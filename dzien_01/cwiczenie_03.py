miasto_a=str(input("Miasto poczatkowe: "))
miasto_b=str(input("Miasto koncowe: "))
dystans=int(input("Podaj odleglosc: "))
cena_paliwa=float(input("Podaj cene paliwa: "))
spalanie=float(input("Podeaj spalanie na 100km: "))


spal_dystans=dystans/spalanie
koszt_podrozy=cena_paliwa*spal_dystans

print("Twoj koszt podrozy z", miasto_a, "do", miasto_b, "to", koszt_podrozy, "PLN")
