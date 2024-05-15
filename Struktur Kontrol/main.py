def main():
    totalBeli = int(input("Masukkan banyak pembelian: "))
    hargaPaket = 990000
    totalAwal = totalBeli * hargaPaket

    if totalBeli >= 10 and totalBeli <= 19:
        diskon20 = (totalBeli * hargaPaket) * 20 / 100
        print(f'Diskon = Rp.{diskon20:10,.2f}')
        duapul = totalAwal - diskon20
        print(f'Total = Rp.{duapul:10,.2f}')
    
    elif totalBeli >= 20 and totalBeli <= 49:
        diskon30 = (totalBeli * hargaPaket) * 30 / 100
        print(f'Diskon = Rp.{diskon30:10,.2f}')
        tigapul = totalAwal - diskon30
        print(f'Total = Rp.{tigapul:10,.2f}')
    
    elif totalBeli >= 50 and totalBeli <= 99:
        diskon40 = (totalBeli * hargaPaket) * 40 / 100
        print(f'Diskon = Rp.{diskon40:10,.2f}')
        empatpul = totalAwal - diskon40
        print(f'Total = Rp.{empatpul:10,.2f}')

    elif totalBeli >= 100:
        diskon50 = (totalBeli * hargaPaket) * 50 / 100
        print(f'Diskon = Rp.{diskon50:10,.2f}')
        limpul = totalAwal - diskon50
        print(f'Total = Rp.{limpul:10,.2f}')
    else:
        totalBeli * hargaPaket
        print(f'Total = Rp.{totalAwal:10,.2f}')

main()

# def main():
#     g = int(input('Masukkan gaji Anda: '))
#     l = int(input('Lama bekerja (tahun): '))
#     if g>=3000000 and l>=2:
#         print(f'Anda terkualifikasi untuk menerima pinjaman!')
#     else:
#         print(f'Anda tidak terkualifikasi untuk menerima pinjaman!')
    
# main()


# i = 2
# while(i <= 100):
#     print(i);
#     i += 2;

# for i in range(50, 0, -2):
#     print(i);
