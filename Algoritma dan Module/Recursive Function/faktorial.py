def faktorial(n):
    if (n == 1):
        return 1
    else:
        return n * faktorial(n - 1)

def main():
    n = int(input("Masukkan nilai n: "))
    print(f"{n}! = {faktorial(n)}")

main()
