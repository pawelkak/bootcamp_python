x=int(input("Podaj X: "))
y=int(input("Podaj Y: "))

if x>90 and y>90:
    print("Prawy gorny rog")
elif x>90 and 0<y<10:
    print("Prawy dolny rog")
elif 0<x<10 and 0<y<10:
    print("Lewy dolny rog")
elif 0<x<10 and y>90:
    print("Lewy gorny rog")
elif x>100 or y>100:
    print("Poza obszarem")
elif 11<x<89 and y>90:
    print("Gorna krawedz")
elif  11<x<89 and y<11:
    print("dolna krawedz")
elif x>90 and 11<y<89:
    print("Prawa krawedz")
elif 11<x<89 and 11<y<89:
    print("Centrum")
else:
    print("Blad parametrow")

    