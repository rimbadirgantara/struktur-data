from os import system as sy
sy('cls')

print('Percobaan 1: Inisialisasi queue')
antrian = []
print(type(antrian))

print('\nPercobaan 2: Menambahkan elemen ke antrian')
antrian.append('No Urut.1')
antrian.append('No Urut.2')
antrian.append('No Urut.3')
antrian.append('No Urut.4')
antrian.append('No Urut.5')
print(f'Daftar Antrian -> {antrian}')

print('\nPercobaan 3: Mengeluarkan elemen dari antrian')
print('Simulasi dequeue')
print(f'Selesai untuk, {antrian.pop(0)}\n{antrian}\n')
print(f'Selesai untuk, {antrian.pop(0)}\n{antrian}\n')
print(f'Selesai untuk, {antrian.pop(0)}\n{antrian}\n')
[print(f'Selesai untuk, {antrian.pop(0)}\n{antrian}\n')
 for i in range(len(antrian))]
