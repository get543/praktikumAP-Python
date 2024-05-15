# Program ini meminta pengguna memasukkan dua angka untuk operasi pembagian
# Program menampilkan pesan jika terjadi eksepsi
def main():
    # [1] Tuliskan statement try/except
    # Pada body klausa try:
    #     - Minta dua angka ke pengguna
    #     - Lakukan pembagian
    # Pada body klausa except untuk ValueError
    #     - Tampilkan pesan: "Nilai yang diinput salah."
    # Pada body klausa except untuk ZeroDivisionError
    #     - Tampilkan pesan: "Tidak dapat membagi dengan nol."
    try:
        bagi = int(input("Masukkan sebuah angka yang akan dibagi: "))
        pembagi = int(input("Masukkan sebuah angka pembagi: "))

        hasil = float(bagi / pembagi)
        print(f"{bagi} dibagi dengan {pembagi} sama dengan {hasil}")

    except ZeroDivisionError:
        print("Tidak dapat membagi dengan nol.")
    except ValueError:
        print("Nilai yang diinput salah.")











# Panggil fungsi main
main()