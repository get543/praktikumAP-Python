def kali(x, y, z=0):
    # base case
    if (y < 1):
        return z
    
    # recursive case
    return kali(x, y-1, z=z+x)



def main():
    x = 4
    y = 3

    print(f"{x} x {y} = {kali(x, y)}")

main()