def bsort(a):
    for i in range(len(a) - 1, 0, -1):
        # print(i, '\n')
        for n in range(i):
            if a[n] > a[n + 1]:
                a[n], a[n + 1] = a[n + 1], a[n]
                # a[n + 1] = a[n]


def gnum(longnum):
    for i in reversed(range(longnum)):
        print(i, end=',')


def binarySearch(a, cari):
    from time import sleep as sl
    ba, bak = 0, len(a) - 1
    s = False
    # while not s and ba <= bak:
    while ba <= bak and not s:
        # while ba <= bak and not s:
        psi = (ba + bak) // 2
        print(f'[PROSES]Mencari nilai {cari} di index {psi}')
        sl(0.5)
        if a[psi] == cari:
            s = True
        elif cari < a[psi]:
            bak = psi - 1
        else:
            ba = psi + 1
    if s == True:
        print(f'\n[SUKSES] Data ditemukan! berada di index {psi}')
    else:
        print(f'\n[GAGAL] Nilai {cari} tidak ditemukan')


a = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(f'Data sebelum di sorting : {a}')
cari = 17
bsort(a)
print(
    f'Data sesudah di sorting : {a}\nJumlah elemen : {len(a)}\nJumlah Index {len(a)-1}\n')
binarySearch(a, cari)

# gnum(1000)
