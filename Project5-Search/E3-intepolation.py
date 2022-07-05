'''
Algoritma Deskriptif
buatlah sebuah function 'interpolation_search' yang mempunyai argument 'array_numsp[], array_size, n(nilai yang dicari)'.
kemudian buatlah beberapa variabel 'lower_pos' bernilai 0, 'higher_pos' bernilai 'array_size - 1'.
setelah itu buatlah perulangan while do dengan kondisi 'lower_pos' lebih kecil sama dengan 'higher_pos' dan 'n' lebih lebih besar sama dengan 'array_nums[lower_por]' dan 'n' lebih kecil sama dengan 'array_nums[higher_pos]' jika kondisi while do false, kembalikan nilai -1, dan jika hasil true maka input 'lower_post +((n - array_nums[lower_pos] * (higher_pos) / (array_nums[higher_pos] - array_nums[lower_pos])))', kemudian lakukan pengecekan jika 'n' lebih besar dari 'array_nums[n_pos]' jika hasil nya false lakukan pengecelan lagi, jika 'n' lebih kecil dari 'array_nums[n_post]' menghasilkan false maka kembalikan nilai 'n_post' dan jika hasil nya true maka input hasil dari 'n_pos - 1' ke dalam 'higher', lalu kembali ke atas. Jika hasil dari 'n > array_nums[n_pos]' true, maka input hasil dari 'n_post + 1' kedalam 'lower_pos' lalu kembali ke atas.

setelah itu inputkan hasil dari function 'interpolation_search' kedalam variabel 'index', kemudian lakukan pengecekan, jika hasil dari 'index' tidak sama dengan -1 maka data ditemukan, jika false, data tidak ditemukan.
'''


def interpolationSearch(arr, lo, hi, x):
    # Kondisi data sudah terurut
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) * (x - arr[lo]))

        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            return interpolationSearch(arr, pos + 1, hi, x)

        if arr[pos] > x:
            return interpolationSearch(arr, lo, pos - 1, x)
    return -1


arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
n = len(arr)
x = int(input(f'Data : {arr}\nSearch ? '))
index = interpolationSearch(arr, 0, n - 1, x)
if index != -1:
    print("Data ditemukan pada index :", index)
else:
    print("Data tidak ditemukan")
