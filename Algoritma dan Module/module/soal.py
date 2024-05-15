# [1] import module yang Anda tulis
import segitigasiku

# Fungsi main menguji module 
def main():
    
    # [2] Minta pengguna untuk memasukkan alas dan tinggi
    alas = int(input("Masukkan panjang alas (cm): "))
    tinggi = int(input("Masukkan tinggi (cm): "))


    
    # [3] Hitung luas dan keliling dengan menggunakan fungsi pada module
    luas = segitigasiku.luas(alas, tinggi)
    keliling = segitigasiku.keliling(alas, tinggi)


    
    # [4] Tampilkan luas dan keliling dengan presisi 2 desimal
    print(f"Luas segitiga: {luas:.2f} cm2")
    print(f"Keliling segitiga: {keliling:.2f} cm")



# Panggil fungsi main
main()