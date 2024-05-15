def generasi_username(nama_depan, nama_belakang, id):
  set1 = nama_depan[0:3].lower() # 3 huruf pertama
  set2 = nama_belakang[0:3].lower() # 3 huruf pertama
  set3 = id[-4:] # angka terakhir

  username = set1 + set2 + set3

  return username

def validasi_password(password):
  panjang_benar = False
  ada_huruf_besar = False
  ada_huruf_kecil = False
  ada_digit = False

  if (len(password) >= 7):
    panjang_benar = True
    for character in password:
      if (character.isupper()):
        ada_huruf_besar = True
      
      if (character.lower()):
        ada_huruf_kecil = True
      
      if (character.isdigit()):
        ada_digit = True

  if (panjang_benar and ada_huruf_besar and ada_huruf_kecil and ada_digit):
    is_valid = True
  else:
    is_valid = False
  
  return is_valid


def main():
  nama = input("Masukkan nama anda: ")
  id = input("Masukkan id mahasiswa anda: ")

  nama_list = nama.split()

  username = generasi_username(nama_list[0], nama_list[1], id)
  print(f"\nUsername Anda: {username}")

  password = input("Masukkan password baru anda: ")

  while not validasi_password(password):
    print("Password yang anda masukkan tidak valid")
    password = input("Masukkan password baru anda: ")

  print("Password anda valid")


main()