i = 0
while True:
    print("Dziala")
    i += 1
    if i == 7:
        break

i = 0
while i < 7:
    print("dzialam")
    i += 1

i = 0
while i < 7:
    if i == 5:
        i += 1
        continue  # jak dojdzie do 5 to nie wykona printowania "i" tylko wroci na poczatek
    print(i)
    i += 1

i = 0
while i < 7:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print("zakonczono")
