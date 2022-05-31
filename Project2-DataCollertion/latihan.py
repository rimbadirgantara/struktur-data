# lib untuk membersihkan layar
from os import system as sy
sy('cls')

nama = ['rimba', 'yanto', 'payos', 'sarep', 'roosvelt']

print('a Menampilkan semua nilai elemen')
print('- dengan for')
[print(x) for x in nama]
print('- dengan while')
i = 0
while i < len(nama):
    print(f'{i+1}. {nama[i]}')
    i += 1

print('b Menampilkan nilai list dengan range 1:4 dan :3')
print(f'List -> {nama}\nRange 1:4')
print(nama[1:4], '\nRange :3')
print(nama[0:3])

print('\nc. Mengubah nilai list dengan range 2:3')
nama[2:3] = ['asri', 'rimba']
print(nama)

print('\nd. tambahkan elem list dengan appen, insert, extend')
nama.append('asdf')
print(f'Dengan append -> {nama}')
nama.insert(6, 'cia')
print(f'Dengan insert -> {nama}')
nama.extend(['a', 'b', 'd', 'e'])
print(f'Dengan testing -> {nama}')

print('\ne. Menghapus elemen list dengan perintah remove, pop, del')
nama.remove('a')
print(f'Dengan remove -> {nama}')
nama.pop(8)
print(f'Dengan pop -> {nama}')
del nama[8]
print(f'Dengan del -> {nama}')

print('\nf. copy list')
print(f'Sebelum copy -> {nama}')
nama = nama.copy()
print(f'Sesudah copy -> {nama}')
nama = list(nama)
print(f'sesudah list -> {nama}')

print('\ng. Penggabungan join, dengan operator +, append dan extend')
print(f'Sebelum join, append, extend -> {nama}')
nama = nama + [1, 2, 3]
print(f'Dengan + -> {nama}')
for x in nama:
    nama.append(x)
print(f'Dengan append -> {nama}')
nama.extend(['7', '8', 9])
print(f'Dengan extend -> {nama}')
