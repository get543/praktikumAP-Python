import math;

# Fungsi luas_lingkaran
def luas_lingkaran(r):
    return math.pi * r * r;
    
# Fungsi keliling_lingkaran():
def keliling_lingkaran(r):
    return math.pi * (2 * r);


# Fungsi main
def main():
    radius = float(input("Masukkan radius lingkaran (cm): "));

    luas = luas_lingkaran(radius);
    keliling = keliling_lingkaran(radius);

    print(f"Luas lingkaran dengan radius {radius:.2f} = {luas:.2f} cm2");
    print(f"Keliling lingkaran dengan radius {radius:.2f} = {keliling:.2f} cm");
    
# Panggil fungsi main
main()
    