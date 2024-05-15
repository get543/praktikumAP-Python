
#! Yang ini mah tamat aja

def sortir(data):
    data.sort()
    return data

def median(data):
    sorted_data = sortir(data)
    
    if (len(sorted_data) % 2 == 0):
        return float(sorted_data[int(len(sorted_data)/2-1)]) + 0.5
    else:
        return sorted_data[int((len(sorted_data)-1)/2)]

def main():
    data = [35, 73, 90, 65, 23, 86, 43, 81, 34, 58]
    data_tersortir = median(data)
    print(data_tersortir)

main()