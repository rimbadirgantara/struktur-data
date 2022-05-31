from os import system as sy
sy('cls')
# Mengenal set
print("a. Mengenal set")
sepedaMotor1 = {"honda", "vario", "150 cc"}
print("sepedaMotor1 = ", sepedaMotor1)
# set tidak dapat memiliki 2 atau lebih item yang sama
sepedaMotor2 = {"honda", "vario", "150 cc", "vario"}
print("sepedaMotor2 = ", sepedaMotor2)
print(type(sepedaMotor1))
print("\nMenghitung panjang set")
print("sepedaMotor1 = ", len(sepedaMotor1))
print("sepedaMotor2 = ", len(sepedaMotor2))
# set dapat memiliki item yang berbeda tipe data
print("\nMemuat item dengan berbagai tipe data")
sepedaMotor3 = {"honda", "vario", "150 cc", 2022}
print("sepedaMotor3 = ", sepedaMotor3)
print("\nCara cek tipe suatu variabel")
print("tipe sepedaMotor1 = ", type(sepedaMotor1))
print("tipe sepedaMotor2 = ", type(sepedaMotor2))
print("tipe sepedaMotor3 = ", type(sepedaMotor3))
print("\nMembuat set dengan konstruktor 'set()'")
sepedaMotor4 = set(("honda", "vario", "150 cc", 2022))
print("sepedaMotor4 = ", sepedaMotor4)

# mengakses item set
print("\nb. Mengakses item set")
'''
Perhatian !
Untuk percobaan berikut, masih menggunakan set sebelumnya
sehingga harus teliti dan cermat mengerjakan percobaan ini.
'''
print("Menggunakan perintah loop for")
print("contoh 1")
for x in sepedaMotor1:
    print(x)
print("\ncontoh 2")
for y in sepedaMotor2:
    print(y)
print("\nMelakukan pengecekan suatu item dengan perintah 'in'")
print("contoh 1")
print("honda" in sepedaMotor1)
print("\ncontoh 2")
print(2022 in sepedaMotor2)


# menambah item set
print("\nc. Menambah item set")
print("\nMenggunakan perintah 'add'")
sepedaMotor1.add("matic")
print(sepedaMotor1)
print("\nMenggunakan perintah 'update'")
print("Contoh 1 - item tambahan bersumber dari set")
updateSP1 = {"hitam", "tubles"}
sepedaMotor1.update(updateSP1)
print("item tambahan dalam bentuk set = ", updateSP1)
print("set sepedaMotor1 hasil update = ", sepedaMotor1)
print("\nContoh 2 - item tambahan bersumber dari list")
updateSP2 = {"hitam", "tubles"}
sepedaMotor2.update(updateSP2)
print("item tambahan dalam bentuk list = ", updateSP2)
print("set sepedaMotor2 hasil update = ", sepedaMotor2)

# menghapus item set
print("\nd. Menghapus item set")
print("Menggunakan perintah 'remove'")
sepedaMotor1.remove("150 cc")
print(sepedaMotor1)
print("\nMenggunakan perintah 'discard'")
sepedaMotor1.discard("tubles")
print(sepedaMotor1)
print("\nMenggunakan perintah 'pop'")
sepedaMotor1.pop()
print(sepedaMotor1)
print("\nMenggunakan perintah 'clear'")
sepedaMotor1.clear()
print(sepedaMotor1)
print("\nMenggunakan perintah 'del'")
# del sepedaMotor1  # HATI-HATI, silahkan dicoba, apa yang terjadi
# print(sepedaMotor1)

# Join set
print("\ne. Join set")
'''
Perhatian !
Untuk percobaan berikut, masih menggunakan set sebelumnya
sehingga harus teliti dan cermat mengerjakan percobaan ini.
'''
print("Menggunakan perintah 'union'")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
print("\nMenggunakan perintah 'update'")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
print("\nMenggunakan perintah 'intersection_update'")
set4 = {"apple", "banana", "cherry"}
set5 = {"google", "microsoft", "apple"}
set4.intersection_update(set5)
print(set4)
print("\nMenggunakan perintah 'intersection'")
set4 = {"apple", "banana", "cherry"}
set5 = {"google", "microsoft", "apple"}
set6 = set4.intersection(set5)
print(set6)
print("\nMenggunakan perintah 'symmetric_difference_update'")
set4 = {"apple", "banana", "cherry"}
set5 = {"google", "microsoft", "apple"}
set4.symmetric_difference_update(set5)
print(set4)
print("\nMenggunakan perintah 'symmetric_difference'")
set4 = {"apple", "banana", "cherry"}
set5 = {"google", "microsoft", "apple"}
set6 = set4.symmetric_difference(set5)
print(set6)
