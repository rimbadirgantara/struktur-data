from nntplib import GroupInfo
from os import system as sy
from pstats import FunctionProfile
sy('cls')
# Mengenal list
print('Percobaa 1 mengenal list')
buah = ['apel', 'pisang', 'cherry']
print(buah)

buah = ['apel', 'pisang', 'cherry', 'apel']
print(buah)
print(type(buah))  # mengetahui tipe list

# konstruktor list
buah = list(('apel', 'pisang', 'cherry'))
print(buah)
print(type(buah))
print('\n')

# mengakses nilai list
print('Percobaan 2 mengakses nilai list')
fruits = ['apel', 'pisang', 'cherry', 'mangga', 'durian', 'manggis']
print(fruits)

print('fruits[0] : ' + fruits[0])
print('fruits[1] : ' + fruits[1])
print('fruits[2] : ' + fruits[2])
print('fruits[-1] : ' + fruits[-1])
print('fruits[-2] : ' + fruits[-2])
# akses menggunakan range
print('menggunakan range')
print(fruits[2:5])
print(fruits[:5])
print(fruits[-5:-2])
print('\n')

# mengubah nilai list
print('Percobaan 3 mengubah nilai list')
print(f'LIST => {fruits}')
fruits[1] = 'banana'
print(fruits)
fruits[3:5] = ['blackcurrant', 'watermelon']
print(fruits)
fruits[3:4] = ['jeruk', 'lengkeng']
print(fruits)
fruits[3:5] = ['semangka']
print(fruits)
print('\n')

print('Percobaan 4 menambah nilai list')
print(f'LIST => {fruits}')
fruits.append('rambutan')
print(fruits)
fruits.insert(1, 'nenas')
print(fruits)
tropis = ['pepaya', 'jambu']
fruits.extend(tropis)
print(fruits)
print('\n')

print('Percobaan 5 Menghapus list')
print('Menggunakan remove')
fruits.remove('semangka')
print(fruits)
print('Menggunakan pop')
fruits.pop()
print(fruits)
fruits.pop(1)
print(fruits)
print('Menggunakan del')
del fruits[1]
print(fruits)
# print('Menggunakan clear')
# fruits.clear()
print(fruits)
print('\n')

print('Percobaan 6 Pengulanan (loop) list')
print('a. menggunakan loop for (versi 1)')
for x in fruits:
    print(x)

# Menggunakan loop for (versi 2)
print('\nb. Menggunakan for - range - len')
for i in range(len(fruits)):
    print(fruits[i])

print('\nc. Cara singkat for')
[print(x) for x in fruits]

print('\nd. Menggunakan while')
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1
print('\n')

print('Percobaan 7 Copy list')
print('a. Perintah copy()')
buahBuahan = fruits.copy()
print(buahBuahan)
print('\nb. Perintah list()')
buahBuahan2 = list(fruits)
print(buahBuahan2)
print('\n')

print('Percobaan 8 join list')  # menggunakan operator +
print('a. Operator')
print(f'buahBuahan 1 => {buahBuahan} \nbuahBuahan2 => {buahBuahan2}')
buahBuahan3 = buahBuahan + buahBuahan2
print(buahBuahan3)

print('\nb. Perintah append')
for x in buahBuahan2:
    buahBuahan.append(x)
print(buahBuahan)

print('\nc. Perintah extend')
buahBuahan2.extend(buahBuahan)
print(buahBuahan2)
