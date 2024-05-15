def linear_search(num, data):
    for index in range(len(data)):
        if (num == data[index]):
            return index
    
    return -1

def main():
    num = 73
    data = [23, 34, 35, 43, 58, 65, 73, 81, 86, 90]

    index = linear_search(num, data)

    if (index == -1):
        print("Data tidak ditemukan")
    else:
        print(f"Data ditemukan pada index ke-{index}")

main()