from os import system as sy
sy('cls') # saya gunakan untuk membersihkan layar saat program ini saya jalankan
angka = [1, 2, 3, 4, 5]
nama = ['Budi', 'Reno', 'Kaori', 'Eren', 'Mikasa']
benda = ['Kursi', 'Keyboard', 'LCD', 'Mouse']
merek = ['Canon', 'Divipard', 'Honda', 'Xiomi']
kata_sifat = ['keras', 'lembut', 'basah', 'cair']

def d(array_):
    for data in array_:
        print(data)

print('a. Menampilkan semua nilai elemen array')
d(angka)
d(nama)
d(benda)
d(merek)
d(kata_sifat)
print('\n')

print('b. Menghitung panjang array')
print(len(angka))
print(len(nama))
print(len(benda))
print(len(merek))
print(len(kata_sifat))
print('\n')


print('c. Menghubah nilai elemen array')
nama[0] = 'Siska'
benda[1] = 'Projector'
print(nama)
print(benda)
print('\n')


print('d Menambah elemen array')
nama.append('Roy')
benda.append('Lampu')
merek.append('Oppo')
print(nama)
print(benda)
print(merek)
print('\n')

print('e. Menyisip elemen array')
nama.insert(1, 'Mongol')
benda.insert(2, 'Obeng')
print(nama)
print(benda)
print('\n')


print('f. Menghapus elemen array')
nama.remove('Mongol')
benda.pop(1)
print(nama)
print(benda)
print('\n')


print('g. Mengurutkan elemen array')
nama.sort(reverse=True)
benda.sort(reverse=False)
print(nama)
print(benda)
print('\n')