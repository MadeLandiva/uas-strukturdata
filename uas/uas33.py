def binary_search_rekursif(a, cari, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if a[mid] == cari:
        return mid
    elif a[mid] < cari:
        return binary_search_rekursif(a, cari, mid + 1, high)
    else:
        return binary_search_rekursif(a, cari, low, mid - 1)


data = input("Masukkan elemen-elemen data: ").split()
data = [int(x) for x in data]
cari = int(input("Masukkan yang ingin dicari: "))

data.sort()

result = binary_search_rekursif(data, cari, 0, len(data) - 1)

if result != -1:
    print("Elemen ditemukan pada indeks:", result)
else:
    print("Elemen tidak ditemukan dalam data.")