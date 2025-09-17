def calculator():
    num1 = float(input("Masukkan Angka Pertama : "))
    operator = input("Masukkan Operator (+ - x /) : ")
    num2 = float(input("Masukkan Angka Kedua : "))
    if operator == "+":
        hasil = num1 + num2
    elif operator == "-":
        hasil = num1 - num2
    elif operator == "/":
        if num2 != 0:
            hasil = num1 / num2
        else:
            return print("Galat! Tidak bisa dibagi dengan 0")
    elif operator.lower() == "x":
        hasil = num1 * num2
    else:
        return print("Operator tidak valid!")
    print(f"Hasil dari {num1} {operator} {num2} = {hasil}")

calculator()