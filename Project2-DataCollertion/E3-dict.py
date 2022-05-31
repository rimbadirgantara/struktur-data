from os import system as sy
sy('cls')
bio = {
    "nama": "Rimba Dirgantara",
    "umur": 19,
    "tempat_tinggal": "Rusun",
    "status": "singel yang ganss",
    "tinggi": 175.9
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


t_item(bio, "rekor_dunia", "ngehek nasa")
print(f'1.{bio}')
t_item(bio, "meretas", "online.sim.polbeng")
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
fck_dict = {
    'pertama': bio,
    'kedua': {
        'situs_terhek': 'online.sim.polbeng',
        'hacking_tool': 'nmap'
    },
    'ketiga': {
        'angka': [1, 2, 3, 4, 5]
    }
}


def loop_dict(var):
    for i, a in fck_dict.items():
        v = (i, fck_dict[i])
        print(v)


loop_dict(fck_dict)
