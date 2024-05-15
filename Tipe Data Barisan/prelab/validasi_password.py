# Fungsi in melakukan validasi password
def validasi_password(passwd):
  spesial_karakter = ['$', '@', '#', '%']
  
  # Variabel-variabel untuk menyimpan hasil pengujian ketentuan. Inisialisasi dengan False.
  panjang_benar = False
  ada_digit = False
  ada_huruf_besar = False
  ada_huruf_kecil = False
  ada_spesial_karakter = False

  # [1] Mulai validasi dengan uji panjang karakter
  # Untuk menguji adanya digit, huruf besar, huruf kecil, dan spesial karakter, gunakan loop yang mengiterasi passwd

  if (len(passwd) >= 6 and len(passwd) <= 20):
    panjang_benar = True

    for character in passwd:
      if (character.isdigit()):
        ada_digit = True

      if (character.isupper()):
        ada_huruf_besar = True
      
      if (character.lower()):
        ada_huruf_kecil = True

      if (character in spesial_karakter):
        ada_spesial_karakter = True

   

  # [2] Jika semua ketentuan terpenuhi tetapkan sebuah varibel untuk nilai kembali dengan True
  # dan selain itu tetapkan dengan False
  if (panjang_benar and ada_huruf_besar and ada_huruf_kecil and ada_digit and ada_spesial_karakter):
    is_valid = True
  else:
    is_valid = False
  

  # [3] Kembalikan variabel nilai kembali yang didapatrkan dari [2]
  return is_valid
    

# is_valid = validasi_password('Budi99#')
is_valid = validasi_password('Password1234')
# is_valid = validasi_password('pass')
# is_valid = validasi_password('Rahasia1234##')

print(is_valid)