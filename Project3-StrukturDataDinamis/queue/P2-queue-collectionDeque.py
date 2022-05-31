try:
    from collections import deque as de
    from os import system as sy
except Exception as e:
    print(f'[ERROR] {e}')

sy('cls')

print('Percobaan 1: inisialiasasi queue')
antrian = de()
print(type(antrian))

print('\nPercobaan 2: Menambah elemen ke antrian')
antrian.append('No Urut.1')
antrian.append('No Urut.2')
antrian.append('No Urut.3')
antrian.append('No Urut.4')
antrian.append('No Urut.5')
print(f'\nDaftar antrian\n{antrian}')

print('\nPercobaan 3: mengeluarkan elemen dari antrian')
print('Simulasi dequeue')
print(antrian.popleft(), '\n', antrian, '\n')
print(antrian.popleft(), '\n', antrian, '\n')
print(antrian.popleft(), '\n', antrian, '\n')
[print(antrian.popleft(), '\n', antrian, '\n') for i in range(len(antrian))]
