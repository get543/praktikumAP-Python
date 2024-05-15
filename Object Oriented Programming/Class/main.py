#[1] import module yang anda buat
import pet

#Fungsi main menguji module
def main():

    #[2] Minta pengguna menginput nama, jenis dan umur
    nama = input("Siapa nama hewan peliharaan Anda? ")
    jenis = input("Jenis hewan apa peliharaan Anda? ")
    umur = int(input("Berapa umur hewan peliharaan Anda? "))

    #[3] Buat objek hewan
    hewan = pet.Pet(nama, jenis, umur)
    nama_hewan = hewan.get_nama()
    jenis_hewan = hewan.get_jenis()
    umur_hewan = hewan.get_umur()
    
    #[4] Tampilkan nama, jenis dan umur
    print(f"Nama: {nama_hewan}")
    print(f"Jenis hewan: {jenis_hewan}")
    print(f"Umur (tahun): {umur_hewan}")


def module():
    '''Pengujian module tanpa fungsi main dengan kode berikut:'''
    import pet

    kitty = pet.Pet('Kitty', 'Kucing', '3')
    print('Nama:', kitty.get_nama())
    print('Jenis:', kitty.get_jenis())
    print('Umur (tahun):', kitty.get_umur())
    print()
    print('Set nama, jenis, dan umur berbeda.')
    kitty.set_nama('Zara')
    kitty.set_jenis('Kucing Persia')
    kitty.set_umur('4')
    print('Nama:', kitty.get_nama())
    print('Jenis:', kitty.get_jenis())
    print('Umur (tahun):', kitty.get_umur())

#Panggil fungsi main
main()
