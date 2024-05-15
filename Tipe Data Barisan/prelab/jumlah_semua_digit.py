# Program ini menghitung jumlah digit-digit dari angka yang dimasukkan pengguna
def main():
  # [1] Minta input ke pengguna
  input_angka = input("Masukkan sebuah angka: ")
  
  # [2] Buat sebuah variabel akumulator
  jumlah = 0
  
  # [3] Iterasi karakter-karakter (digit-digit) dalam string angka yang dimasukkan pengguna
  # dan konversi ke integer untuk mendapatkan representasi integer dari digit
  for angka in input_angka:
    jumlah += int(angka)

  # [4] Tampilkan jumlah digit dengan teks: "Jumlah digit-digit dari <input_angka_pengguna> = <jumlah_digit>"
  print(f"Jumlah digit-digit dari {input_angka} = {jumlah}")

    
# Panggil fungsi main
main()