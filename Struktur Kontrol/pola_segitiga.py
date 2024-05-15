# pola_segitiga.py
# Program ini mencetak pola segitiga
def main():
    banyaknya = int(input("Masukkan sebuah angka: "))

    for baris in range(banyaknya, 0, -1):
        for kolom in range(baris):
            print('*', end='')
        print()
main()