# Fungsi ini mencari nilai maksimum dari sebuah list secara rekursif
def maksimum_rekursif(data, index = 0):
    # Tuliskan kode Anda di bawah.
    # [1] Gunakan statement if bersarang untuk mencari nilai maksimum
    # [2] Statement if bagian pertama memastikan jumlah data ada lebih dari 1 elemen
    # [3] Statement if bagian kedua (didalam if bagian pertama) menentukan apakah elemen pertama list lebih besar dari elemen lainnya

    if (index == len(data)): return None

    max_sisa = maksimum_rekursif(data, index + 1)

    element_sekarang = data[index]

    if ((max_sisa is None) or (element_sekarang > max_sisa)):
        return element_sekarang
    else:
        return max_sisa




def main():
    angka = [23, 45, 12, 98, 45, 67, 88]

    print(f"nilai max adalah {maksimum_rekursif(angka)}")

main()