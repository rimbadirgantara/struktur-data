from os import system as sy  # import lib os
sy('cls')
ordo = [[11, 12], [13, 14]]
ordo2 = [[15, 16], [17, 18]]


def d(ordo):
    for x in range(0, len(ordo)):
        for y in range(0, len(ordo[0])):
            print(ordo[x][y], end=' ')
    print()


print('A. Menampilkan semua \nnilai elemen matrik dengan perintah for')
d(ordo)
print('\n')

print('B. Lakukan operasi arimatika berikut ini')
print('1. Penjumlahan')
for x in range(0, len(ordo)):
    for y in range(0, len(ordo[0])):
        print(ordo[x][y] + ordo2[x][y], end=' ')
    print()
print('\n')

print('2. Pengurangan')
for x in range(0, len(ordo)):
    for y in range(0, len(ordo[0])):
        print(ordo[x][y] - ordo2[x][y], end=' ')
    print()
print('\n')

print('3. Perkalian')
for x in range(0, len(ordo)):
    for y in range(0, len(ordo[0])):
        print(ordo[x][y] * ordo2[x][y], end=' ')
    print()
