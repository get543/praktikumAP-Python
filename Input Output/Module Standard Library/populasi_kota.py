# [1] Import module math
import math;

# Fungsi hitung_populasi
# [2] Tuliskan parameter-parameter yang diperlukan
def hitung_populasi(populasi_awal, t):
    # [3] Hitung populasi setelah waktu t. Gunakan fungsi dalam module math.
    # Bulatkan ke bawah hasil penghitungan (hilangkan nilai desimalnya). Misal: hasil penghitungan 754595.685 maka nilai
    # yang dikembalikan fungsi ini adalah 754595.
    populasi_akhir = populasi_awal * math.pow(math.e, (0.1 * t));

    return populasi_akhir;
    
    
    
    
    

# Fungsi main
def main():
    # [4] Minta input pengguna untuk populasi awal. Prompt 'Masukkan populasi awal: '
    populasi = int(input("Masukkan populasi awal: "));
    
    
    # [5] Minta input pengguna untuk waktu. Prompt 'Masukkan waktu dalam tahun: '
    tahun = int(input("Masukkan waktu dalam tahun: "));
    
    
    # [6] Hitung populasi setelah waktu t dengan memanggil fungsi hitung_populasi
    nilai_populasi_akhir = hitung_populasi(populasi, tahun);


    # [7] Tampilkan populasi akhir: Populasi akhir = <nilai_populasi_akhir>
    print(f"Populasi akhir = {math.floor(nilai_populasi_akhir)}");
    
    
    
# Panggil fungsi main
main()