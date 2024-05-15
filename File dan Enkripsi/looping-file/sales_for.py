# Program ini menghitung rata-rata penjualan
# dengan data yang terdapat dalam file sales.txt
def main():
    
    # Ikuti petunjuk pada komentar di bawah.
    # Petunjuk pada kerangka program ini menggunakan 3 langkah menggunakan file: buka, proses, tutup.
    # Anda diperbolehkan menggunakan statement with, namun kode Anda akan sedikit berbeda dengan petunjuk di bawah

    
    # [1] Buat dua buah variabel: variabel penghitung baris untuk menghitung banyak baris (untuk digunakan sebagai banyak penjualan)
    # dan variabel akumulator untuk menghitung total penjualan
    isi_baris = 0
    total_penjualan = 0
    
    
    # [2] Buka file sales.txt untuk dibaca dan simpan object file ke suatu variabel
    with open("sales.txt", "r") as file:

        # [3] Baca baris pertama isi file dan simpan ke suatu variabel

    
        # [4] Tuliskan loop while untuk mengiterasi isi file setiap barisnya dan lakukan hal berikut pada setiap iterasi:
        # - akumulasikan isi_baris ke variabel akumulator (jangan lupa konversi ke tipe numerik)
        # - inkrementasi variabel penghitung baris
        for baris in file:
            baris_bersih = baris.rstrip("\n") #* bisa di vscode
            # baris_bersih = baris.rstrip() #* bisa di praktikum

            if (baris_bersih):
                isi_baris += 1
                total_penjualan += float(baris_bersih)


    
    
    
    
    # [5] Hitung rata-rata dengan membagi total penjualan dan banyak penjualan (variabel akumulator / variabel penghitung baris)
    # dan tampilkan hasilnya.

    # print(f"isi baris : {isi_baris}, tipe data: {type(isi_baris)}")
    # print(f"total penjualan : {total_penjualan}, tipe data: {type(total_penjualan)}")

    hasil = total_penjualan / isi_baris
    print(f"Rata-rata penjualan: {hasil:,.2f}")
    



# Panggil fungsi main
main()