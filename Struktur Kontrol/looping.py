### Looping longkap 2
# i = 2;
# while(i <= 100):
#     print(i);
#     i += 2;

### Looping pangkat 2 buat hasilnya
# for i in range(1, 11):
#     print(i ** 2);

### Looping mundur longkap 2
# for i in range(50, 1, -2):
#     print(i);

### Nested Looping
# for x in range(10):
#   for y in range(10):
#     print(x, y)

### Masukkin angka 10 kali abis tu hasilnya di tambahin
# def main():
#     total = 0
    
#     for i in range(1, 11):
#         num = int(input('Masukkan angka: '))
#         total += num

#     print(f'Total = {total}')

# main();



# Program ini menghitung rata-rata dari rangkaian input yang dimasukkan pengguna
def main():
    counter = 0;
    total = 0;
    
    num = int(input("Masukkan angka positif (akhiri dengan memasukkan angka negatif): "));
    
    if (num < 0):
        return print(f"Rata-rata angka yang dimasukkan: 0");

    while num > 0:
        counter += 1;
        total += num;
        totalAkhir = total / counter;
        
        num = int(input("Masukkan angka positif (akhiri dengan memasukkan angka negatif): "));
        
    print(f"Rata-rata angka yang dimasukkan: {totalAkhir}");
    

# Panggil fungsi main
main()