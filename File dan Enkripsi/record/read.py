# Program ini membaca record nilai mahasiswa
# dari file nilai_mahasiswa.txt
def main():

    # [1] Buka file nilai_mahasiswa.txt dengan statement with untuk dibaca
    # Pada body statement with:
    # - Gunakan loop while untuk membaca field-field dari semua record
    # - Tampilkan record dengan tampilan:
    #           Nama: <nama_mahasiswa>
    #           Nilai: <nilai_mahasiswa>
    
    with open("nilai_mahasiswa.txt", "r") as file:
        nama = "t"

        while nama != "":
            nama = file.readline().rstrip("\n")
            nilai = file.readline().rstrip("\n")

            print(f"Nama: {nama}")
            print(f"Nilai: {nilai}")
            print()

# ! yang ini bener su beda dikit doang lah tot
#     with open('nilai_mahasiswa.txt','r') as nilai_file:
#         baris = 'a'
#         while baris != '':
#             baris = nilai_file.readline()
#             if baris == '':
#                 continue
#             baris = baris.rstrip('\n')
#             print(f'Nama: {baris}')
#             baris = baris.rstrip('\n')
#             baris = nilai_file.readline()
#             print(f'Nilai: {baris}')












# Panggil fungsi main
main()