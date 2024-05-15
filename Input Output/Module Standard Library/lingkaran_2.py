import math;

def luas_lingkaran(radius):
    return math.pi * radius * radius;

def main():
    radius = float(input("Masukkan radius lingkaran (cm): "));
    luas = luas_lingkaran(radius);
    print(f"Luas lingkaran dengan radius {radius:.2f}: {luas:.2f} cm2");

main();