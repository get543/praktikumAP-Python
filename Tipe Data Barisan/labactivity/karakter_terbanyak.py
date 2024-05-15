def main():
    karakter_list = []
    banyak_karakter = {}

    string = input("Masukkan sebuah teks: ").lower()

    for karakter in string:
        if karakter in banyak_karakter:
            banyak_karakter[karakter] += 1
        else:
            banyak_karakter[karakter] = 1

    karakter_paling_sering = max(banyak_karakter, key=banyak_karakter.get)
    print(f"Karakter terbanyak: {karakter_paling_sering}")


main()
