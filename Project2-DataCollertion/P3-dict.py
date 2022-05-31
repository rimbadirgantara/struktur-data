from os import system as sy
sy('cls')
# mengenal dict
print('a. Percobaan 1, Mengenal Dictionaries')
sepedaMotor = {
    "produsen": "honda",
    "jenis": "matic",
    "model": "vario",
    "mesin": "150 cc",
    "tahunProduksi": 2022
}
print(sepedaMotor)
print(sepedaMotor["produsen"])
print(sepedaMotor["tahunProduksi"])
print('\n')

# dict tdiak bisa memiliki key yang sama
sepedaMotor2 = {
    "produsen": "honda",
    "jenis": "matic",
    "model": "vario",
    "model": "vario",
    "mesin": "150 cc",
    "tahunProduksi": 2022,
    "tahunProduksi": 2022
}
print(sepedaMotor)

# dict bisa memiliki value lebih dari satu untuk satu key, contoh
sepedaMotor3 = {
    "produsen": "honda",
    "jenis": "matic",
    "model": "vario",
    "mesin": "150 cc",
    "tahunProduksi": [2022, 2021, 2020]
}
print(sepedaMotor3)
# mengetahui panjang dict
print(len(sepedaMotor3))
# mengetahui apakah suatu variabel berjenis dict atau tidak
print(type(sepedaMotor3))
print('\n')

print('b. Percobaan 2 mengakses dict')
sepedaMotor = {
    "produsen": "honda",
    "jenis": "matic",
    "model": "vario",
    "mesin": "150 cc",
    "tahunProduksi": 2022
}
a = sepedaMotor["model"]
b = sepedaMotor["mesin"]
print(a)
print(b, "\n")

print("menggunakan perintah get()")
c = sepedaMotor.get("produsen")
d = sepedaMotor.get("tahunProduksi")
print(c, '\n', d, '\n')

# mengetahui key yang ada di dict
print("Menggunakan perintah keys()")
kunci = sepedaMotor.keys()
print(kunci, '\n')

# menambah key baru di dict 'sepedaMotor'
print('menambahkan key')
sepedaMotor['warna'] = 'hitam'
print(sepedaMotor)

# perintah values() untuk mengetahui nilai/value yang ada di dict
print('\nMenggunakan perintah values()')
nilai = sepedaMotor.values()
print(nilai)
sepedaMotor['warna'] = 'putih'
print(nilai, '\n')

# perintah intems() untuk mengetahui key:value
print('\nMenggunakan perintah items()')
item = sepedaMotor.items()
print(item)

print('\nCara pengecekan key di dict')
if "produsen" in sepedaMotor:
    print("key 'produsen' ada di dict 'sepedaMotor'")

print('\nC. Percobaan 3 Mengubah item dict')
sepedaMotor['model'] = 'Supra'
print(item)

print('\nMenggunakan perintah update()')
sepedaMotor.update({"jenis": "non metic"})
print(item)

print('\nD. Percobaan 4 menambah item dict')
sepedaMotor['negaraProdusen'] = "indonesia"
print(item)
print('\nMenggunakan perintah update()')
sepedaMotor.update({"noMesin": "SPR202202"})
print(item)

print('\nE. Percobaan 5 menghapus item dict')
print('menggunakan perintah pop')
sepedaMotor.pop('noMesin')
print(item)
print('\nMenggunakan perintah popitem()')
sepedaMotor.popitem()
print(item)

print('\nMenggunakan perintah del')
del sepedaMotor['warna']
print(item)
# Menghapus dict
# del sepedaMotor

print('\nMenggunakan perintah clear()')
sepedaMotor.clear()
print(item)

print('\nF. Percobaan 6, Pengulangan di dict')
print('Mencetak key')
print('versi 1')
for i in sepedaMotor2:
    print(i)

print('\nversi 2')
for j in sepedaMotor2.keys():
    print(j)

print('\n Mencetak value')
print('versi 1')
for k in sepedaMotor2:
    print(sepedaMotor2[k])

print('\nVersi 2')
for l in sepedaMotor2.values():
    print(l)

print('\nMencetak Key dan Value')
for m, n in sepedaMotor2.items():
    print(m, n)

print('\nG. Percobaan 7 Penggandaan (copy) dict')
print('Menggnukan perintah copy()')
mirror1_sepedaMotor2 = sepedaMotor2.copy()
print(mirror1_sepedaMotor2)
print('\nMenggunakan perintah dict()')
mirror2_sepedaMotor2 = dict(sepedaMotor2)
print(mirror2_sepedaMotor2)

print('\nH. Percobaan 8 Nested dict')
print('sebuah dict dapat memuat dict')
print('\nContoh 1')
mobil = {
    "produsen": "toyota",
    "brand": "veloz"
}
mobil2 = {
    "produsen": "daihatsu",
    "brand": "xenia"
}
mobil3 = {
    "produsen": "mitshubisi",
    "brand": "xpander"
}
mobil4 = {
    "produsen": "nissan",
    "brand": "livina"
}
jenisMobil = {
    "jenis1": mobil,
    "jenis2": mobil2,
    "jenis3": mobil3,
    "jenis4": mobil4,
}
for o, p in jenisMobil.items():
    print(o, p)

print('\nContoh 2')
tipeMobil = {
    "jenis1": {
        "produsen": "toyota",
        "brand": "veloz"
    },
    "jenis2": {
        "produsen": "daihatsu",
        "brand": "xenia"
    },
    "jenis3": {
        "produsen": "mitsubisi",
        "brand": "xpander"
    },
    "jenis4": {
        "produsen": "nissan",
        "brand": "livina"
    }
}
for q, r in tipeMobil.items():
    print(q, r)
