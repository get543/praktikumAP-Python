# Fungsi binary search rekursif menerapkan
# algoritma binary search secara rekursif
def binary_search_rekursif(num, data, index = 0):
    # [1] Base Cases
    # Jika data kosong (panjang = 0) tidak ada yang bisa dicari
    # kembalikan -1
    if (len(data) == index):
        return -1
    elif (len(data) == 0):
        return -1
    
    # [2] Recursive Cases
    # Jika data tidak kosong, dapatkan indeks tengah dari data
    # Struktur seleksi:
    # 1. Jika elemen tengah sama dengan num kembalikan indeks tengah
    # 2. Jika elemen tengah lebih besar, lakukan pemanggilan rekursif terhadap paruh atas data
    # 3. Jika elemen tengah lebih kecil, lakukan pemanggilan rekursif terhadap paruh bawah data
    if (data[index] != num):
        return binary_search_rekursif(num, data, index + 1)
    elif (data[index] == num):
        return index

def main():
    print(binary_search_rekursif(34, [23, 26, 31, 34, 45, 67, 90]))
    print(binary_search_rekursif(98, [23, 26, 31, 34, 45, 67, 90]))

main()