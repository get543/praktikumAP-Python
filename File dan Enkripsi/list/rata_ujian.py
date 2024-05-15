# Program ini membaca file daftar_nilai.txt yang berisi data nilai ujian
# dari 30 mahasiswa dan mencari nilai rata-rata, nilai tertinggi, dan nilai terenda
def main():
    
    # Buat variabel untuk menyimpan hasil perhitungan dan inisialisasi dengan 0.0 (float)
    rata_rata = 0.0
    nilai_tertinggi = 0.0
    nilai_terendah = 0.0
    isi_baris = 0
    nilai_nilai = []
    
    # [1] Tuliskan statement untuk membuka file daftar_nilai.txt untuk dibaca 
    # dan simpan isinya ke sebuah list
    with open("daftar_nilai.txt", "r") as file:



        
        # [2] Tuliskan struktur loop untuk menghapus karakter baris baru pada setiap elemen
        # dari list
        for baris in file:
            baris_bersih = baris.rstrip("\n")

            if (baris_bersih):
                rata_rata += float(baris)
                isi_baris += 1
                nilai_nilai.append(float(baris))
                




    
    # [3] Cari nilai rata-rata, nilai tertinggi, dan terendah. Gunakan loop.
    nilai_tertinggi = max(nilai_nilai)
    nilai_terendah = min(nilai_nilai)
    hasil_rata_rata = rata_rata / isi_baris
    
    
    # [4] Tampilkan rata-rata, nilai tertinggi, dan nilai terendah.

    print(f"Rata-rata nilai ujian: {hasil_rata_rata}")
    print(f"Nilai ujian tertinggi: {nilai_tertinggi}")
    print(f"Nilai ujian terendah: {nilai_terendah}")




    
    
# Panggil fungsi main()
main()