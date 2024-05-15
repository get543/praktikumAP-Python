def main():
    detik = int(input("Masukkan jumlah detik: "))

    if (detik >= 86400):
        hari = detik // 86400
        jam = (detik // 3600) % 24
        menit = (detik // 60) % 60
        detik = detik % 60
        print(f"{hari} hari {jam} jam {menit} menit {detik} detik")

    elif (detik >= 3600):
        jam = (detik // 3600) % 24
        menit = (detik // 60) % 60
        detik = detik % 60
        print(f"{jam} jam {menit} menit {detik} detik")

    elif (detik >= 60):
        jam = (detik // 3600) % 24
        menit = (detik // 60) % 60
        detik = detik % 60
        print(f"{menit} menit {detik} detik")

main()