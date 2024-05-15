
#! Nyerah gw asli dah susah bener

def indeks_minimum(data):
    return data

def selection_sort_rekursif(data, sorted=[]):
    if ((len(data) == 1) or (len(data) == 0)):
        return data
    elif ((len(data)) == (len(sorted))):
        return sorted

    data.sort(reverse=True)

    if (len(sorted) == 0):
        sorted.append(data[-1])
        return selection_sort_rekursif(data, sorted)
    else:
        sorted.append(data[-(len(sorted)+1)])
        return selection_sort_rekursif(data, sorted)


def main():
    data = [35, 73, 90, 65, 23, 86, 43, 81, 34, 58]
    data_tersortir = selection_sort_rekursif(data)
    print(data_tersortir)

main()