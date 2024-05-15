# try:
#     x = float('abc123')
#     print('Konversi berhasil.')
# except IOError:
#     print('Kode ini menyebabkan IOError.')
# except ValueError:    
#     print('Kode ini menyebabkan ValueError.')

try:
    y = int('x1010')
    print(y)
except IOError:
    print('Kode ini menyebabkan IOError.')
except ZeroDivisionError:
    print('Kode ini menyebabkan ZeroDivisionError.')
except:
    print('Sebuah error terjadi.')