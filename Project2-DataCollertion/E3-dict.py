bio = {
    "nama": "Muhammad Viekri Alfarisi",
    "umur": 19,
    "tempat_tinggal": "Bengkalis",
    "status": "Pacaran",
    "tinggi": 180.2
}

print('a. Menampilkan semua item dengan perintah loop')
for key_, value_ in bio.items():
    print(f"{key_}:{value_}")

print('\nB. Pengecekan terhadap key tertentu (3 key)')


def cek_key(the_key, the_var):
    if the_key in the_var:
        the_varr = the_var[the_key]
        print(f"key '{the_key}' ada di dict '{the_varr}'")
    else:
        print(f'key "{the_key}" tidak ditemukan')


cek_key('nama', bio)
cek_key('umur', bio)
cek_key('nama_doi', bio)

print('\nC. Penambahan item (minimal 2 item)')


def t_item(var, key, value):
    var[key] = value
    return var[key]


t_item(bio, "hoby", "poly")
print(f'1.{bio}')
t_item(bio, "makanan", "sate")
print(f'2.{bio}')

print('\nPengubah item dengan perintah pop (1 item), popitem (1 popitem)')
print('1. POP')
bio.pop('nama')
print(bio)
bio.popitem()
print(bio)

print('\nE. Copy dict')
mirr_bio = bio.copy()
print(mirr_bio)

print('\nF. Nested dict')
new_dict = {
    'pertama': bio,
    'kedua': {
        'hoby': 'poly',
        'makanan': 'sate'
    },
    'ketiga': {
        'angka': [1, 2, 3, 4, 5]
    }
}


def loop_dict(var):
    for i, a in new_dict.items():
        v = (i, new_dict[i])
        print(v)


loop_dict(new_dict)
