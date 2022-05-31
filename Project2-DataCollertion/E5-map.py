from os import system as sy
sy('cls')


def menghitungMapDenganlen(i):
    return len(i)


def penjumlahan(a, b):
    return a + b


def tampilkanitem(var_string):
    for i in range(len(var_string)):
        print(f'- {var_string[i]}')


cewe = ('asri', 'ime', 'lastri', 'roma', 'ranita')
musik = ('pulau samosir', 'sai anju ahu', 'sayur kol', '2 phut hon', 'bad guy')
print(f'Variabel 1 : {tuple(cewe)}')
print(f'Variabel 2 : {tuple(musik)}')
print('\na. menghitung map dengan perintah len')
this_map_f = map(menghitungMapDenganlen, cewe)
print(f'Jumlah map : {this_map_f}')

print('\nb. Menampilkan item menggunakan list')
print(f'List : {list(this_map_f)}')

print('\nc. Menggabungkan(menjumlahkan) 2 list dan hitung map hasil penggabungan')
c = map(penjumlahan, list(cewe), list(musik))
print(f'Jumlah map : {c}')
print(f'list : {list(c)}')

print('\nd. Menampilkan item dari 2 list')
print('list 1')
tampilkanitem(cewe)
print('list 2')
tampilkanitem(musik)
