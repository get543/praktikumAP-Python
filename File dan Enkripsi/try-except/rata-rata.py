def main():
    # List untuk menyimpan isi file
    list_angka = []
    isi_baris = 0
    rata_rata = 0
    
    # [1] Tuliskan statement yang meminta pengguna memasukkan nama file dengan prompt: Masukkan nama file: "
    nama_file = input("Masukkan nama file: ")

    
    # [2] Tuliskan exception handler dengan statement try/except
    # Pada body klausa try: buka file, baca isinya, dan simpan isinya ke list_angka
    # Pada body klausa except untuk FileNoFoundError tampilkan pesan "File tidak ditemukan."
    # Pada body klausa except untuk ValueError tampilkan pesan "Terdapat data non numerik dalam file."
    # Pada body klausa else: Cari rata-rata, nilai tertinggi, nilai terenda dan tampilkan hasilnya
    try:
        with open(nama_file, "r") as file:
            for baris in file:
                baris_bersih = baris.rstrip("\n")
                
                if (baris_bersih):
                    isi_baris += 1
                    rata_rata += float(baris)
                    list_angka.append(float(baris))
                    
    except FileNotFoundError:
        print("File tidak ditemukan.")
    except ValueError:
        print("Terdapat data non numerik dalam file.")
    else:
        rata_rata = rata_rata / isi_baris
        nilai_tertinggi = max(list_angka)
        nilai_terendah = min(list_angka)
        
        print(f"Rata-rata nilai: {rata_rata:.2f}")
        print(f"Nilai tertinggi: {nilai_tertinggi:.2f}")
        print(f"Nilai terendah: {nilai_terendah:.2f}")
    
    
    
    
    
    
    
    
    
    
    
    
# Panggil fungsi main
main()