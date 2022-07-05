from os import system as sy
sy('cls')


def bsearch(a, search):
    awal, akhir, ketemu = 0, len(a) - 1, False
    while awal <= akhir and not ketemu:
        tengah = (awal + akhir) // 2
        if a[tengah] == search:
            ketemu = True
        else:
            if search < a[tengah]:
                akhir = tengah - 1
            else:
                awal = tengah + 1
    return ketemu


a = [1, 2, 3, 4, 5, 6]
search = int(input('Search ? '))
print(bsearch(a, search))
