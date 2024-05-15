# Tuliskan definisi class Orang, Siswa, dan Pekerja di bawah.
class Orang:
    def __init__(self, nama, umur):
        self.__nama = nama
        self.__umur = umur

    def tampilkan_nama(self):
        return print(f"Nama saya adalah {self.__nama}")

    def tampilkan_umur(self):
        return print(f"Umur saya adalah {self.__umur}")


class Siswa(Orang):
    def __init__(self, nama, umur, tingkat):
        Orang.__init__(self, nama, umur)
        self.__tingkat = tingkat

    def tampilkan_tingkat(self):
        return print(f"Saya tingkat {self.__tingkat}")


class Pekerja(Orang):
    def __init__(self, nama, umur, pekerjaan):
        Orang.__init__(self, nama, umur)
        self.__pekerjaan = pekerjaan

    def tampilkan_pekerjaan(self):
        return print(f"Pekerjaan saya {self.__pekerjaan}")


def main():
    orang1 = Orang('Budi Susilo', 33)
    siswa1 = Siswa('Andi Geledek', 17, '12')
    pekerja1 = Pekerja('Tomi Gunawan', 32, 'Wiraswasta')

    print('Informasi orang 1:')
    orang1.tampilkan_nama()
    orang1.tampilkan_umur()
    print()

    print('Informasi siswa 1:')
    siswa1.tampilkan_nama()
    siswa1.tampilkan_umur()
    siswa1.tampilkan_tingkat()
    print()

    print('Informasi pekerja 1:')
    pekerja1.tampilkan_nama()
    pekerja1.tampilkan_umur()
    pekerja1.tampilkan_pekerjaan()


main()
