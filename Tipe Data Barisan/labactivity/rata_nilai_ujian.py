def main():
    # Constant untuk Jumlah Ujian (Kolom)
    # dan Jumlah Mahasiswa (Baris)
    JUMLAH_UJIAN = 3
    nilai_ujian = []

    JUMLAH_MHS = int(input("Masukkan jumlah mahasiswa: "))

    for mahasiswa in range(1, JUMLAH_MHS + 1):
        print("=============================================")
        print(f"Masukkan nilai ujian untuk mahasiswa {mahasiswa}")
        print("---------------------------------------------")

        nilai1 = float(input("Masukkan nilai ujian ke-1: "))
        nilai2 = float(input("Masukkan nilai ujian ke-2: "))
        nilai3 = float(input("Masukkan nilai ujian ke-3: "))

        nilai_ujian.append([nilai1, nilai2, nilai3])

    print("=============================================")

    # Iterasi setiap mahasiswa (baris)
    for mhs in range(JUMLAH_MHS):
        # Akumulator nilai ujian
        total_nilai = 0

        # Iterasi nilai ujian dari mahasiswa mhs (kolom)
        for ujian in range(JUMLAH_UJIAN):
            total_nilai += nilai_ujian[mhs][ujian]

        # Hitung rata-rata ujian
        rerata = total_nilai / JUMLAH_UJIAN

        # Tampilkan rata-rata nilai ujian setiap mahasiswa
        print(f'Rata-rata ujian mahasiswa {mhs + 1}: {rerata:.2f}')


# Panggil fungsi main
main()
