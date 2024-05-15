# Fungsi ini meminta pengguna memasukkan rangkaian angka-angka
# dan menggunakan sentinel untuk mengakhiri input angka.
# Fungsi ini mengembalikan sebuah list yang berisi angka-angka yang diinput pengguna
def get_score():
  # Buat list kosong untuk menyimpan angka-angka yang dimasukkan pengguna
  score_list = []
  
  while True:
    # [1] Minta penggunakan memasukkan skor berupa angka
    score = int(input("Masukkan skor (masukkan angka negatif untuk menyudahi): "))

    # [2] Tulis struktur loop yang meminta pengguna memasukkan angka-angka
    if (score < 0):
      break
    else:
      score_list.append(score)
      

  return score_list

print(get_score())