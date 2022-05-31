from os import system as sy
sy('cls')
# Mengenal map
print("a. Mengenal map")
print("Contoh 1")


def menghitungPanjang(i):
    return len(i)


j = map(menghitungPanjang, ("honda", "vario", "150 cc"))
print("Panjang map = ", j)
print("Panjang masing-masing item : ", list(j))
print("\nContoh 2")


def penjumlahan(m, n):
    return m + n


data = map(penjumlahan, ("honda", "vario", "150 cc"), ("hitam", "tubles"))
print(data)
print(list(data))
