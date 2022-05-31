from os import system as sy
sy('cls')
# Mengenal tuple
print('A. Percobaan 1, Mengenal tuple')
fruits1 = ("apple", "banana", "cherry")
print(fruits1)
fruits2 = ("apple", "banana", "cherry", "apple")
print(fruits2)
fruits3 = ("apple",)
print(type(fruits3))
# contoh yang tidak termasuk tuple
fruits4 = ("apple")
print(type(fruits4))
# contoh lain tuple
tuple1 = (1, 5, 7, 9, 3)
print(tuple1)
tuple2 = (True, False, False)
print(tuple2)
tuple3 = ("abc", 34, True, 40, "male")
print(tuple3)
# membuat tuple dengan kontrusktor tuple()
fruits5 = tuple(("apple", "banana", "cherry"))  # Ingat !!
# Gunakan tanda kurung 2x
print(fruits5)

print('\nB. Percobaan 2, Mengakses tuple')
fruits = ("apel", "pisang", "cherry", "mangga", "durian",
          "manggis")
print(fruits)
print("fruits[0] : " + fruits[0])
print("fruits[1] : " + fruits[1])
print("fruits[2] : " + fruits[2])
print("fruits[-1] : " + fruits[-1])
print("fruits[-2] : " + fruits[-2])
# akses menggunakan range
print(fruits[2:5])
print(fruits[:5])
print(fruits[-5:-2])
print(fruits[2:])
# akses dengan kondisi if
if "apel" in fruits:
    print("Apel ada di tuple fruits")

print('\nC. Percobaan 3, Mengubah nilai tuple')
fruits = ("apel", "pisang", "cherry", "mangga", "durian", "manggis")
buah = list(fruits)  # konversi tuple menjadi list
buah[1] = "kiwi"
fruits = tuple(buah)  # konversi list menjadi tuple
print(fruits)

print('\nD. Percobaan 4, Menambahkan nilai tuple')
# menggunakan perintah append
print("Menggunakan perintah append")
fruits = ("apel", "pisang", "cherry", "mangga", "durian",
          "manggis")
buah = list(fruits)
buah.append("orange")
fruits = tuple(buah)
print(fruits)
# menambah tuple ke dalam tuple
print("Menambah tuple kedalam tuple")
fruits = ("apel", "pisang", "cherry", "mangga", "durian", "manggis")
buahBaru = ("rambutan", "sirsak",)
fruits += buahBaru
print(fruits)

print('\nE. Percobaan 5 menghapus nilai tuple')
# menggunakan perintah remove
print("Menggunakan perintah remove")
fruits = ("apel", "pisang", "cherry", "mangga", "durian", "manggis")
buah = list(fruits)
buah.remove("apel")
fruits = tuple(buah)
print(fruits)
# menggunakan perintah del
# del fruits  # HATI-HATI, perintah del menghapus tuple
# print(fruits)

print('\nF. Percobaan 6, Unpack tuple')
fruits = ("apel", "pisang", "cherry", "manggis")
(buah1, buah2, buah3, buah4) = fruits  # proses unpack
tuple
print(buah1)
print(buah2)
print(buah3)
print(buah4)
# penggunaan asterik (*)
print("Menggunakan perintah asterik *")
fruits = ("apel", "pisang", "cherry", "mangga", "durian",
          "manggis")
print("versi 1")
(buah1, buah2, *buah3) = fruits
print(buah1)
print(buah2)
print(buah3)
print("versi 2")
(buah1, *buah2, buah3) = fruits
print(buah1)
print(buah2)
print(buah3)

print('\nG. Percobaan 7, Loop tuple')
fruits = ("apel", "pisang", "cherry", "mangga", "durian", "manggis")
print("\nPerintah for")
for x in fruits:
    print(x)
print("\nKombinasi for, range, dan len")
for i in range(len(fruits)):
    print(fruits[i])
print("\nPerintah While")
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1

print('\nH. Percobaan 8, Join tuple')
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
# operator +
tuple3 = tuple1 + tuple2
print(tuple3)
# operator *
tuple4 = tuple1 * 2
print(tuple4)
tuple5 = tuple2 * 3
print(tuple5)

print('\nI. Percobaan 9, Method di tuple')
tuple6 = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# perintah count
print("Menghitung kuantiti nilai tertentu di tuple")
x = tuple6.count(5)
print(x)
# perintah index
print("Mencari nilai tertentu di tuple")
x = tuple6.index(3)
# y = tuple6.index(9)  # error karna 9 tidak ada di dalam tuple
print(x)
# print(y)
