from os import system as sy  # import lib os
sy('cls')
print("Percobaan 1 : Mengenal matrik")
print("-----------------------")
print('A. Membuat Matrik Ordo 2x2')
mA = [
    [32, 12],
    [23, 20]
]
print(mA)
mB = [
    [45, 24],
    [50, 21]
]
print(mB)
print("-----------------------")
print('\n')

print("Percobaan 2 : Menampilkan nilai matrik")
print("-----------------------")
print('B. Menampilkan nilai Matrik')
print(mA[0][0])
print(mA[1][1])
print(mB[1])
print("-----------------------")
print('\n')

print("Percobaan 3 : Menampilkan nilai matrik dengan perintah for")
print("-----------------------")
print('C. Menampilkan nilai Matrik dengan perintah for')
for x in range(0, len(mA)):
    for y in range(0, len(mA[0])):
        print(mA[x][y], end=' ')
    print()
print('\n')


print("Percobaan 4 : Operator aritmatika (penjumlahan) matrik")
print("-----------------------")
print('D. Operasi Arimatika Matrik - Penjumlahan')
print(mA)
print(mB)
tambah1 = mA[0][0] + mB[0][0]
print(tambah1)
tambah2 = mA[0][1] + mB[0][1]
print(tambah2)
print("-----------------------")
print('\n')


print("Percobaan 5 : Operator aritmatika (pengurangan) matrik")
print("-----------------------")
print('E. Operasi Arimatika matrik - pengurangan')
print(mA)
print(mB)
for x in range(0, len(mA)):
    for y in range(0, len(mA[0])):
        print(mA[x][y] - mB[x][y], end=' ')
    print()
print('\n')
