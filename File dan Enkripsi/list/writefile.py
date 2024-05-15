angka = [234, 694, 123, 789, 923, 674, 534]

with open('daftar_angka.txt', 'w') as output_file:
    for element in angka:
        output_file.write(str(element) + "\n")
