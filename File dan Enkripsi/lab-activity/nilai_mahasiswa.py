# Program ini membaca record nilai mahasiswa
# dari file nilai_mahasiswa.txt
def main():

    # Variabel sebagai penanda jika nama mahasiswa yang dicari ditemukan
    found = False
    
    try:
        # [1] Tuliskan statement untuk meminta nama file ke pengguna
        # Gunakan prompt: 'Masukkan nama file: '
        nama_file = input("Masukkan nama file: ")
        
        # [2] Tuliskan staement untuk membuka file dengan nama file yang diberikan pengguna
        # Anda dapat menggunakan statement with atau 3 langkah menggunakan file: buka, proses, tutup.
        with open(nama_file, "r") as file:
            # [3] Tampilkan pesan: "File <nama_file> berhasil dibuka.". Tambahkan baris baru.
            print(f"File {nama_file} berhasil dibuka.")
            
            # [4] Tuliskan statement untuk meminta nama mahasiswa yang ingin dicari
            # Gunakan prompt: 'Masukkan nama mahasiswa yang ingin dicari: '
            cari_mahasiswa = input("\nMasukkan nama mahasiswa yang ingin dicari: ")
            
            # [5] Tuliskan statement untuk membaca baris pertama dari file (nama mahasiswa).
            baris = "fh"
            
            # [6] Tuliskan loop while yang mengiterasi baris-baris file 
            while baris != "":
                # [7] Tuliskan statement untuk membaca nilai mahasiswa
                baris = file.readline()
                
                if (baris == ""): continue
                
                # [8] Tuliskan statement untuk menghilangkan baris baru pada nama mahasiswa dan nilai mahasiswa
                # Gunakan rstrip.
                baris = baris.rstrip("\n")
                
                # [9] Tuliskan struktur seleksi yang menentukan apakah nama mahasiswa cocok
                # dengan nama yang ingin dicari
                if (baris == cari_mahasiswa):
                    # [10] Jika nama_mahasiswa sama dengan nama yang ingin dicari
                    # Tampilkan Nama dan Nilai
                    print(f"Nama Mahasiswa: {baris}")
                    baris = baris.rstrip("\n")
                    baris = file.readline()
                    print(f"Nilai: {float(baris):.2f}")
                    
                    # [11] Tetapkan nilai variabel penanda found dengan True
                    # Ini karena mahasiswa ditemukan
                    found = True

                # [12] Tuliskan statement membaca baris berikutnya
                

    # [13] Tuliskan klausa except FileNotFoundError
    # Pada body klausa except ini tampilkan: File <nama_file> tidak ditemukan.
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")
        
    # [14] Tuliskan klausa else
    # Pada body klausa else tuliskan struktur seleksi jika found tidak sama dengan True
    # tampilkan pesan: "Nama <nama yang dicari> tidak ditemukan."
    else:
        if (found != True):
            print(f"Nama {cari_mahasiswa} tidak ditemukan.")
            

# Panggil fungsi main
main()