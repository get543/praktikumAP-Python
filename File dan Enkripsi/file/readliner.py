# Program ini membaca isi file angka_float.txt
# dan mengalikan angka yang terdapat dalam file tersebut
def main():
    
    # [1] Buka file dengan statement with atau 3 langkah menggunakan file: buka, proses, tutup.
    # Lalu ambil angka pertama pada baris pertama dan angka kedua pada baris kedua, simpan
    # angka pada setiap baris isi file masing-masing ke sebuah variabel 
    with open("angka_float.txt", "r") as file:
        baris1 = file.readline()
        baris2 = file.readline()

    baris1 = baris1.rstrip('\n')
    baris2 = baris2.rstrip('\n')


    # [2] Hitung hasi kali dan tampikan sesuai dengan ketentuan program yang diminta
    hasil = float(baris1) * float(baris2)

    print(f"Baris 1 file angka_float.txt berisi: {baris1}")
    print(f"Baris 2 file angka_float.txt berisi: {baris2}")
    print(f"Hasil kali baris 1 dan baris 2 = {hasil:.2f}")




# Panggil fungsi main
main()