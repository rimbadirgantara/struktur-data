# ngosol (ngoding solo)
def bsort(data_):
    # sorting method = bubble sort
    for n in range(len(data_) - 1, 0, -1):
        for i in range(n):
            if data_[i] > data_[i+1]:
                data_[i], data_[i + 1] = data_[i + 1], data_[i]


def binarySearch(a, b):
    from time import sleep as sl
    s = False
    da = 0
    bk = len(a) - 1
    while not s and da <= bk:
        cari = da + (bk - da) // 2  # 0 + (8 - 0) // 2 = 4
        sl(1)
        print(
            f'[Proses] Posisi Pencarian di index {cari} dengan nilai {a[cari]}')
        if a[cari] == b:
            s = True
        elif a[cari] > cari:
            bk = cari - 1
        else:
            da = cari + 1
    if s == True:
        print(f'\n[Sukses] Nilai {b} Di temukan di index {cari}')
    else:
        print(f'\n[Gagal] Nilai {b} tidak ditemukan')


a = [34, 53, 26, 67, 2, 24, 1, 6, 4, 5, 6, 7, 8,
     9, 10, 11, 12, 13, 14, 15]  # 7 index, 8 elemen
print(f'Data Sebelum BSorting {a}')
bsort(a)
cari = 260
print(f'Data sesudah BSorting : {a}\n')
binarySearch(a, cari)
