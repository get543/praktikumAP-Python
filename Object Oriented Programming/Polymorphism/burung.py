class Burung:
    def __init__(self, spesies):
        self.__spesies = spesies
    
    def tampilkan_spesies(self):
        print(f"Saya adalah seekor {self.__spesies}")

    def buat_suara(self):
        print("Ciut... Ciut...")

class Ayam(Burung):
    def __init__(self):
        super().__init__("ayam")

    def buat_suara(self):
        print("Kukuruyuuuk...")

class Bebek(Burung):
    def __init__(self):
        super().__init__("bebek")

    def buat_suara(self):
        print("Kwek! Kwek!")


def main():
    burung = Burung('burung generik')
    ayam = Ayam()
    bebek = Bebek()

    burung.tampilkan_spesies()
    burung.buat_suara()
    print()

    ayam.tampilkan_spesies()
    ayam.buat_suara()
    print()

    bebek.tampilkan_spesies()
    bebek.buat_suara()

main()