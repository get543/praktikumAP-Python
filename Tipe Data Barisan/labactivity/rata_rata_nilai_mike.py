def main():
    # Minta pengguna untuk memasukkan teks
    input_string = input("Masukkan sebuah teks: ")

    # Konversi input_string menjadi huruf kecil
    input_string = input_string.lower()

    karakter_list = []  # Daftar karakter yang muncul dalam string
    banyak_karakter = []  # Jumlah kemunculan masing-masing karakter

    # Iterasi melalui string input
    for char in input_string:
        if char.isalpha():  # Hanya proses karakter alfabet
            if char in karakter_list:
                # Jika karakter sudah ada dalam karakter_list, tambahkan jumlahnya
                index = karakter_list.index(char)
                banyak_karakter[index] += 1
            else:
                # Jika karakter belum ada dalam karakter_list, tambahkan ke daftar karakter dan inisialisasi jumlahnya
                karakter_list.append(char)
                banyak_karakter.append(1)

    if karakter_list:
        # Temukan karakter dengan jumlah terbanyak
        max_count = max(banyak_karakter)
        max_chars = [karakter_list[i] for i, count in enumerate(
            banyak_karakter) if count == max_count]
        # Ambil karakter pertama jika ada beberapa karakter terbanyak
        max_char = max_chars[0]

        print("Karakter terbanyak: ", max_char)
    else:
        print("Tidak ada karakter alfabet dalam teks yang dimasukkan.")


if __name__ == "__main__":
    main()
