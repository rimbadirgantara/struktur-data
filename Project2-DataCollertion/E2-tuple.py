from os import system as sy
sy('cls')
nama = ('Rimba', 'Rima', 'Aryanto', 'Payos', 'Edy')

print('A. Menampilkan semua nilai lemen tuple dengan perintah loop for, for dengan kombinasi range dan len, while')
print('Dengan For')
for n in nama:
    print(n)
print('\nFor dengan kombinasi range n len')
for nn in range(len(nama)):
    print(nama[nn])
print('\nDengan While Loop')
i = 0
while i < len(nama):
    print(nama[i])
    i += 1

print('\nB. Menampilkan nilai tuple dengan range 1:4, :3, -4:-1, 2:')
print(f'Range 1:4 : {nama[1:4]}')
print(f'Range :3 : {nama[:3]}')
print(f'Range -4:-1 : {nama[-4:-1]}')
print(f'Range 2: : {nama[2:]}')

print('\nC. Mengubah nilai tuple sebanyak 2 elemen')
namaa = list(nama)
namaa[2] = 'Elisa'
namaa[3] = 'Sania'
print(tuple(namaa))

print('\nD. Penambahan elemen pada tuple')
print('Dengan Append')
namaa.append('Febiola')
print(namaa)
namaa += ('Livy', 'joyce')
print(tuple(namaa))

print('\nE. Penghapusan elemen tuple dengan perintah remove')
namaa.remove('Edy')
print(tuple(namaa))

print('\nF. Unpack tuple dengan asterik(*)')
(n1, n2, *n3) = list(namaa)
print(f'{n1}\n{n2}\n{n3}')

print('\nG. Join Tuple')
print('Dengan perintah operator +')
new_nama = list(nama) + namaa
print(new_nama)
print('Dengan perintah operator *')
new_nama = list(nama) * 2
print(new_nama)

print('\nH. Perhitungan kuantiti')
print(f"Jumlah Rima : {namaa.count('Rima')}")
print(f"Jumlah Elisa : {namaa.count('Elisa')}")

print('\nI. Pencarian nilai tertentu')
print(f"{namaa}\nRima berada di index {namaa.index('Rima')}")
print(f"Elisa berada di index {namaa.index('Elisa')}")
print(f"Livy berada di index {namaa.index('Livy')}")
