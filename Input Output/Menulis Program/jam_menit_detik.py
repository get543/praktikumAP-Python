detik = int(input("Masukkan waktu dalam detik: "));

jam = detik // 3600;
menit = (detik % 3600) // 60;
detik %= 60;

print(f"Berikut waktu dalam jam, menit, dan detik:");
print(f"Jam : {jam} \nMenit: {menit} \nDetik: {detik}");
