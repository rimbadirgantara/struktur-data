from os import system as sy
sy('cls')
#Array 1 Dimensi
print('Percobaan 1: Mengenal array')
print('--------------')
print('Array 1 Dimensi')
sisi = 8
siswa = ["Budi", "Charlie", "Erlangga"]
tas = ["eiger","bodypack",5, 12.5]
print(sisi)
print(siswa[0])
print(siswa[1])
print(siswa[2])
print(tas[0])
print(tas[3])
print('\n')

print("Percobaan 2 : Menampilkan semua data/nilai array")
print("-----------------------")
print("Perintah : for ..in")
for data in siswa:
    print(data)
print('\n')

print("Percobaan 3 :Menghitung panjang array")
print("-----------------------")
print("Perintah : len")
panjang = len(siswa)
print(panjang)
print('\n')

print("Percobaan 4 : Mengubah elemen array")
print("-----------------------")
siswa[0] = "suci sekali"
print(siswa)
siswa[2] = "cahyo"
print(siswa)
print('\n')

print("Percobaan 5 : Menambah elemen array")
print("-----------------------")
print("Perintah : append")
siswa.append("dicky")
print(siswa)
siswa.append("ikall")
print(siswa)
siswa.append("cahrlie")
print(siswa)
siswa[5] = "charles"
print(siswa)
print('\n')

print("Percobaan 6 :Menyisip elemen array")
print("-----------------------")
print("perintah : insert")
siswa.insert(1, "Rukhi")
print(siswa)
print('/n')

print("Percobaan 7 : menghapus elemen array")
print("-----------------------")
print("perintah : pop")
siswa.pop(5)
print(siswa)
#Perintah 2: remove, menghapus berdasarkan nilai/value
print('perintah: remove')
siswa.remove("dicky")
print(siswa)
print('\n')

print("Percobaan 8 : mengurutkan elemen array")
print("Perintah : sort")
siswa.sort(reverse = True)
print(siswa)
