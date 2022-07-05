'''
algoritma deskriptif
buatlah function bernama Sequential_Search() yang dapat menerima argument dlist dan item.
setelah itu buat variabel pos dengan nilai 0 dan variabel found dengan nilai false.
lakukan perulangan while do dengan kondisi pos lebih kecil dari jumlah data dlist 
dan variabel found tidak false (true).
setelah hasil dari while do tadi adalah true lakukan pengecekan, apakah variabel 
dlist[pos] nilai nya sama dengan variabel item, jika hasil nya true maka set variabel 
found menjadi true dan while do di stop karna variabel found nilai nya menjadi true, 
lalu kembalikan variabel found dan pos dan data yang dicari ditemukan, dan jika false 
variabel pos di tambah satu.'''


def Sequential_Search(dlist, item):
    pos = 0
    found = False
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos += 1
    return found, pos


a = int(input('Search ? '))

print(Sequential_Search([11, 23, 58, 31, 56, 77, 43, 12, 65, 19], a))
