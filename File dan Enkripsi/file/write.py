# Program ini menuliskan teks "Bandung", "Jakarta", "Depok" masing-masing dalam satu baris ke file kota.txt
def main():
    # [1] Tuliskan statement untuk membuka file kota.txt untuk ditulis dan referensikan object file ke variabel output_file
    file = open("kota.txt", "w")

    
    # [2] Tuliskan statement-statement untuk menulis teks 'Bandung', 'Jakarta', 'Depok' 
    # masing-masing dalam satu baris ke file kota.txt denga method write.
    file.write('Bandung\nJakarta\nDepok\n')


    
    # [3] Tuliskan statement untuk menutup file kota.txt
    file.close()

    
# Panggil fungsi main
main()