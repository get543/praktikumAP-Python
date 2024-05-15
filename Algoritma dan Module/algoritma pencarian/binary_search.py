def binary_search(num, data):
    low = 0
    high = len(data) - 1

    while (low <= high):
        mid = (low + high) // 2

        if (num == data[mid]):
            return mid
        elif (num < data[mid]):
            high = mid - 1
        else:
            low = mid - 1
    
    return -1

def main():
    num = 73
    data = [23, 34, 35, 43, 58, 65, 73, 81, 86, 90]

    index = binary_search(num, data)

    if (index == -1):
        print("Data tidak ditemukan")
    else:
        print(f"Data ditemukana paa index ke-{index}")

main()
