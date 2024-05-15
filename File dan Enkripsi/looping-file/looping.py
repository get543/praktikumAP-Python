# Program ini menuliskan angka 1 s.d 100 
# ke file daftar_angka.txt

# [1] Import module random
import random


# Definisi fungsi main
def main():

    # [2] Tuliskan kode untuk membuka file daftar_angka.txt untuk ditulis
    # Generasi angka acak antara 1 s.d 100 sebanyak 100 angka dengan fungsi randint
    # dan tulis masing-masing angka ke masing-masing baris pada file daftar_angka.txt.

    outfile = open('daftar_angka.txt', 'w')

    for i in range(1, 101):
        outfile.write(str(i) + '\n')

    outfile.close()






# [3] Panggil fungsi main            
main()