# konversi_kilo2.py
# Program ini mengkonversi jarak kilometer ke dalam
# mil. Hasilnya akan ditampilkan ke sebuah dialog box
import tkinter
import tkinter.messagebox


class KonversiKiloGUI:
    def __init__(self):
        # Membuat widget window utama
        self.main_window = tkinter.Tk()
        # Membuat dua frame untuk membentuk grup widget
        self.frame_atas = tkinter.Frame(self.main_window)
        self.frame_tengah = tkinter.Frame(self.main_window)
        self.frame_bawah = tkinter.Frame(self.main_window)
        # Membuat widget untuk frame atas
        self.label = tkinter.Label(
            self.frame_atas, text='Masukkan jarak dalam KM : ')
        self.entry_km = tkinter.Entry(self.frame_atas, width=10)

        # Menggabungkan widget untuk frame atas
        self.label.pack(side='left')
        self.entry_km.pack(side='left')
        # Buatlah widget untuk frame tengah
        self.desk_label = tkinter.Label(
            self.frame_tengah, text='Terkonversi ke dalam mil : ')
        # Dibutuhkan StringVar object untuk mengasosiasikannya
        # dengan sebuah label output. Gunakan method set()
        # untuk menyimpan sting dari karakter kosong
        self.nilai = tkinter.StringVar()
        # Buatlah sebuah label dan hubungkan dengan objek
        # StringVar. Nilai apapun yang disimpan dalam objek# StringVar akan secara otomatis ditampilkan ke
        # dalam label
        self.label_mil = tkinter.Label(
            self.frame_tengah, textvariable=self.nilai)
        # Gabungkan widget pada frame tengah
        self.desk_label.pack(side='left')
        self.label_mil.pack(side='left')
        # Membuat widget tombol untuk frame bawah
        self.tombol_hitung = tkinter.Button(
            self.frame_bawah, text='Konversi', command=self.konversi)
        self.tombol_keluar = tkinter.Button(
            self.frame_bawah, text='Keluar', command=self.main_window.destroy)
        # Gabungkan tombol-tombol
        self.tombol_hitung.pack(side='top')
        self.tombol_keluar.pack(side='top')
        # Gabungkan frame
        self.frame_atas.pack()
        self.frame_tengah.pack()
        self.frame_bawah.pack()
        # Masuk ke dalam loop utama tkinter
        tkinter.mainloop()
        # Method konversi adalah fungsi yang dipanggil
        # ketika tombol_hitung diklik


def konversi(self):
    # Ambil nilai yang diinput pengguna ke dalam widget entry_km
    kilo = float(self.entry_km.get())
    # Konversi kilo ke mil
    mil = kilo * 0.6214
    # Konversi mil ke sebuah string dan simpan ke
    # dalam objek StringVar. Ini akan secara
    # otomatis memperbarui widget label_mil
    self.nilai.set(mil)
    # Membuat instans untuk kelas KonversiKiloGUI
    kilo_mil = KonversiKiloGUI()
