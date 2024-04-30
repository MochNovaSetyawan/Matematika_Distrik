def perkalian(a, b):
    return a * b

def pertambahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def pembagian(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def operasi(pilihan, a, b):
    if pilihan == "1":
        return pertambahan(a, b)
    elif pilihan == "2":
        return pengurangan(a, b)
    elif pilihan == "3":
        return perkalian(a, b)
    elif pilihan == "4":
        return pembagian(a, b)
    else:
        return "Invalid operation"

def info_tampilan():
    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

def input_tampilan():
    pilihan = input("Pilih metode operasi 1/2/3/4 : ")
    a = float(input("Masukan angka pertama : "))
    b = float(input("Masukan angka kedua   : "))
    result = operasi(pilihan, a, b)
    print("Hasil:", result)


info_tampilan()
input_tampilan()

