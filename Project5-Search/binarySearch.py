def bsort(a):
    for i in range(len(a) - 1, 0, -1):
        #print(i, '\n')
        for n in range(i):
            if a[n] > a[n + 1]:
                a[n], a[n + 1] = a[n + 1], a[n]
                #a[n + 1] = a[n]


def gnum(longnum):
    for i in reversed(range(longnum)):
        print(i, end=',')


def binarySearch(a, cari):
    from time import sleep as sl
    ba, bak, s = 0, len(a) - 1, False
    while not s and ba < bak:
        psi = ba + (bak - ba) // 2  # 4 = 12,(5)
        # 5 (7 - 5) // 2  = 6
        # 6 (7 - 5) // 2 = 7
        print(f'Mencari nilai {cari} di index {psi} | Tidak di temukan')
        sl(0.5)
        if a[psi] == cari:
            s = True
        elif a[psi] > cari:
            bak = psi - 1
        else:
            ba = psi + 1
    if s == True:
        print(f'[SUKSES] Data ditemukan! berada di index {psi}')


a = [23, -1, 0, 4, 27, 30, 12, 45, 9]
print(f'Data sebelum di sortint : {a}\n')
cari = 30
bsort(a)
print(f'\nData sesudah di sorint : {a}')
binarySearch(a, cari)

# gnum(100)
