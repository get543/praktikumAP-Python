def main():
    ulang = "y"
    
    while (ulang == "y"):
        angka1 = int(input("Masukkan angka 1: "))
        angka2 = int(input("Masukkan angka 2: "))

        total = angka1 + angka2

        print(f"Jumlah = {total}")

        ulang = input("Masukkan y untuk melanjutkan: ")

main()