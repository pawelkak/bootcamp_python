produkt_1 ="pomidory"
waga_1=10
cena_1=10

produkt_2 ="ogorki"
waga_2=10
cena_2=10

produkt_3 ="banany"
waga_3=11
cena_3=83

suma=cena_1+cena_2+cena_3


raport = f"""

{produkt_1:>30} {waga_1:5.2f} kg; {cena_1:5.2f} PLN
{produkt_2:>30} {waga_2:5.2f} kg; {cena_2:5.2f} PLN
{produkt_3:>30} {waga_3:5.2f} kg; {cena_3:5.2f} PLN

suma:{suma:>30.2f} PLN
"""

print(raport)

