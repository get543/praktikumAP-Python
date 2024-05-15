# Fungsi ini menghitung banyaknya huruf besar dari argumen yang diberikan dan mengembalikan
# jumlah huruf besar.
def banyak_huruf_besar(input_string):
    
  # [1] Buat sebuah variabel penghitung yang digunakan untuk menghitung banyak_huruf_besar dan inisialisasi dengan 0
  huruf_besar = 0

  # [2] Tuliskan loop yang mengiterasi karakter-karakter dalam input_string dan uji apakah karakter tersebut adalah huruf besar
  # dengan method isupper(). Jika ya, inkrementasi variabel penghitung.
  for huruf in input_string:
    if (huruf.isupper()):
      huruf_besar += 1
      

  
  # [3] Kembalikan variabel penghitung
  return huruf_besar

print(banyak_huruf_besar('Halo, Selamat Datang di Universitas Gunadarma'))

print(banyak_huruf_besar('PERHATIKAN INDENTASI!'))