first_number = float(input("podaj pierwsza liczbe: "))
second_number = float(input("podaj druga liczbe: "))
operator = input("podaj operator: ")

if operator == "+":
    print(first_number + second_number)
elif operator == "-":
    print(first_number - second_number)
elif operator == "/":
    print(first_number / second_number)
elif operator == "*":
    print(first_number * second_number)
elif operator == "**":
    print(first_number ** second_number)
else:
    print("Zly operator")
