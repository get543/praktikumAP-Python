import math

def luas(alas, tinggi):
    return alas * tinggi / 2

def keliling(alas, tinggi):
    sisi_miring = math.sqrt((alas ** 2) + (tinggi ** 2))
    return alas + tinggi + sisi_miring