gracz_x=5
gracz_y=5

skarb_x=5
skarb_y=8


while True:
    polecenie=input("Wykonaj ruch (wasd):" )

    if gracz_x>9 or gracz_y>9:
        print("Wypadles poza plansze")
        break

    if polecenie=="w":
        gracz_y+=1
    elif polecenie=="a":
        gracz_y-=1
    elif polecenie=="d":
        gracz_x+=1
    else:
        gracz_x-=1

    print(f"Pozycja gracza: gracz_x={gracz_x} gracz_y={gracz_y}")