# Program ini meminta pengguna memasukkan tiga buah angka float
# dan menuliskan keduanya, masing-masing dalam satu baris, 
# ke file angka.txt
def main():
    
    # [1] Minta pengguna memasukkan tiga buah angka desimal
    # Gunakan prompt "Masukkan sebuah angka desimal: " untuk angka pertama
    # dan prompt "Masukkan sebuah angka desimal lainnya: " untuk angka kedua dan ketiga 
    angka1 = float(input("Masukkan sebuah angka desimal: "))
    angka2 = float(input("Masukkan sebuah angka desimal lainnya: "))
    angka3 = float(input("Masukkan sebuah angka desimal lainnya: "))




    
    # [2] Buka file angka.txt untuk ditulis dan tuliskan angka-angka yang didapat
    # dari pengguna ke file tersebut masing-masing dalam baris baru.
    with open("angka.txt", "a") as file:
        file.write(str(angka1) + "\n")
        file.write(str(angka2) + "\n")
        file.write(str(angka3) + "\n")


        
    
    # [3] Tampilkan pesan "Data telah berhasil disimpan dalam file angka.txt."
    print("Data telah berhasil disimpan dalam file angka.txt.")


    
# Panggil fungsi main
main()