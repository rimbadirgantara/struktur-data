from os import system as sy
sy('cls')
cewe = {'Rima', 'Elean', 'Pebiola', 'Elisa', 'Asri'}

print('a. Menampilkan semua item dengan perintah loop for')
for my_cewe in cewe:
    print(my_cewe)

print('\nb. Pengecekan terhadap item (3 item)')
print('Rima' in cewe)
print('Elisa' in cewe)
print('Eve' in cewe)

print('\nc. Penambahan item')
print('Mengunakan perintah Add')
cewe.add('Jinan')
print(cewe)
print('Menggunakan perintah update')
new_cewe = {'Chika', 'Livy'}
cewe.update(new_cewe)
print(cewe)

print('\nd. Penghapusan item')
print('Dengan perintah remove')
cewe.remove('Chika')
print(cewe)
print('Dengan perintah discard')
cewe.discard('Chika')
print(cewe)
print('Dengan perintah pop')
cewe.pop()
print(cewe)
print('Dengan perintah clear')
cewe.clear()
print(cewe)

print('\ne. Join set')
print('Dengan perintah union')
set1 = {'Rima', 'Elean', 'Pebiola', 'Elisa', 'Asri'}
set2 = {1, 2, 3, 4, 5}
set3 = set1.union(set2)
print(set3)
print('\nDengan perintah update')
set4 = {'Rima', 'Elean', 'Pebiola', 'Elisa', 'Asri'}
set5 = {20, 12, 14, 24}
set4.update(set5)
print(set4)
print('\nDengan perintah intersection_update')
big_platform = {"apple", "banana", "cherry"}
big_platform2 = {"google", "microsoft", "apple"}
big_platform.intersection_update(big_platform2)
print(big_platform)
print('\nDengan perintah intersection')
set4 = {"apple", "banana", "cherry"}
set5 = {"google", "microsoft", "apple"}
set6 = set4.intersection(set5)
print(set6)
print("\nMenggunakan perinta 'symmetric_difference_update'")
set4 = {"apple", "banana", "cherry"}
set5 = {"google", "microsoft", "apple"}
set4.symmetric_difference_update(set5)
print(set4)
print("\nMenggunakan perintah 'symmetric_difference'")
set4 = {"apple", "banana", "cherry"}
set5 = {"google", "microsoft", "apple"}
set6 = set4.symmetric_difference(set5)
print(set6)
