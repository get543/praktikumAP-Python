# Program ini menambahkan record nilai mahasiswa
# ke file nilai_mahasiswa.txt
def main():
    # [1] Minta pengguna berapa banyak record yang ingin dimasukkan
    record_mahasiswa = int(input("Berapa banyak record nilai mahasiswa yang ingin Anda tambahkan? "))

    with open("nilai_mahasiswa.txt", "a") as file:
        for mahasiswa in range(1, record_mahasiswa + 1):
            print(f"Masukkan nilai record mahasiwa ke {mahasiswa}")
            nama = input("Nama: ")
            nilai = input("Nilai: ")
            print()

            # [2] Buka file dengan statement with, minta input masing-masing record ke pengguna, dan tulis ke file nilai_mahasiswa.txt
            file.write(nama + "\n")
            file.write(nilai + "\n")


        
        # ! pake yang ini su
#     with open('nilai_mahasiswa.txt','a') as file_nilai:
#         for i in range(jumlah_mahasiswa):
#             print(f'Masukkan record nilai mahasiswa ke {i+1}')
#             nama = input('Nama: ')
#             nilai = input('Nilai: ')
#             file_nilai.write(f'{nama} \n')
#             file_nilai.write(f'{nilai} \n')
#             print()







# Panggil fungsi main
main()