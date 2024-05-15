# [1] Import module yang telah anda buat
import mahasiswa

# Fungsi main untuk menguji class Mahasiswa
def main():
    
    # [2] Buat tiga object mahasiswa dari class Mahasiswa sesuai dengan data pada tabel
    mahasiswa1 = mahasiswa.Mahasiswa("Budi Susilo", 11223344, "Teknik Informatika", "0811-1234-7896")
    mahasiswa2 = mahasiswa.Mahasiswa("Inggrid Wijaya", 11286755, "Sistem Informasi", "0819-0086-9978")
    mahasiswa3 = mahasiswa.Mahasiswa("Amelia", 11245645, "Ilmu Komunikasi", "0838-7765-0987")
    
    
    # [3] Tampilkan Data Mahasiswa 1
    print(mahasiswa1)

    # [4] Tampilkan Data Mahasiswa 2
    print(mahasiswa2)

    # [5] Tampilkan Data Mahasiswa 3
    print(mahasiswa3)
    
    
# Panggil fungsi main
main()





# def module_test():
#     mhs = mahasiswa.Mahasiswa('Budi Susilo', '11223344', 'Teknik Informatika', '0811-1234-7896')
#     print('Nama:', mhs.get_nama())
#     print('NPM:', mhs.get_npm())
#     print('Jurusan:', mhs.get_jurusan())
#     print('Nomor Telepon:', mhs.get_no_telepon())
#     print()

#     print('Set nama, npm, jurusan, dan nomor telepon berbeda.')
#     mhs.set_nama('Inggrid Wijaya')
#     mhs.set_npm('11286755')
#     mhs.set_jurusan('Sistem Informasi')
#     mhs.set_no_telepon('0819-0086-9978')

#     print('Nama:', mhs.get_nama())
#     print('NPM:', mhs.get_npm())
#     print('Jurusan:', mhs.get_jurusan())
#     print('Nomor Telepon:', mhs.get_no_telepon())
#     print()

# module_test()