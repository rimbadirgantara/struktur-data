# lib untuk membersihkan layar
from os import system as sy
sy('cls')

nama = ['rimba', 'yanto', 'payos', 'sarep', 'roosvelt']

print('a. Menampilkan semua nilai elemen list dengan perintah loop for dan loop while')
print('- for')
[print(f'{my_for+1}. {nama[my_for]}') for my_for in range(len(nama))]
print('\n- while')
i = 0
while i < len(nama):
    print(f'{i+1}. {nama[i]}')
    i += 1

print('\nb. Menampilkan nilai list dengan range 1:4, range :3')
print(f'list nama -> {nama}\nrange 1:4\n{nama[1:4]}\nrange :3\n{nama[:3]}')

print('\nc. Mengubah nilai list dengan range 2:3 (nilai bisa di sesuaikan')
nama[2:3] = ['udin', 'asep']
print(nama)

print('\nd. Penambahan elemen list denga perintah append, insert, dan extend')
nama.append('gabitch')
print(f'Penambahan dengan append -> {nama}')
nama.insert(0, 'evitri')
print(f'Penambahan dengan insert -> {nama}')
nama_baru = ['asri', 'lastri', 'edy']
nama.extend(nama_baru)
print(f'Penambahan dengan extend -> {nama}')

print('\ne. Penghapusan elemen list dengan perintah remove, pop, del')
print(f'dengan perintah remove')
nama.remove("rimba")
print(nama)
print(f'dengan perintah pop')
nama.pop(1)
print(nama)
print('dengan perintah del')
del nama[0]
print(nama)

print('\nf. Mengcopy list dengan perintah copy dan list')
new_ = nama.copy()
print(f'dengan perintah copy\n{new_}')
new__ = list(nama)
print(f'dengan perintah list\n{new__}')

print('\ng. Penggabungan (join) list dengan perintah operator +, append, dan extend')
namaa = nama + nama
print(f'dengan perintah + -> {namaa}')
for x in namaa:
    nama.append(x)
print(f'\ndengan perintah append -> {nama}')
namaa.extend(nama)
print(f'\ndengan perintah extend -> {namaa}')
