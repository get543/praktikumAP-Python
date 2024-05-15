def index_minimum(data):
    indeks_min = 0
    min = data[indeks_min]

    for indeks in range(1, len(data)):
        if data[indeks] <= min:
            indeks_min = indeks
            min = data[indeks_min]

    return indeks_min

def selection_sort():
    data_tersortir = []

    for i in range(len(data)):
        indeks_min = indeks_minimum(data)
        data_tersortir.append(data[indeks_min])
        data.pop(indeks_min)

    return data_tersortir



def main():
    data = [35, 73, 90, 65, 23, 86, 43, 81, 34, 58]
    data_tersortir = selection_sort_rekursif(data)
    print(data_tersortir)

main()