# menghitung total nilai - nilai dalam sebuah list

def main():
  numbers = [2, 4, 6, 8, 10]
  total = 0

  for value in numbers:
    total += value

  print(f"Total dari elemen - elemen adalah {total}")

main()