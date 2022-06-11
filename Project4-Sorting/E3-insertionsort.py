def insertionSort(arr):
    for i in range(1, len(arr)):  # menghasilkan 4 putaran
        key = arr[i]  # value : a (untuk putara 1)
        j = i-1  # value : 0 (putaran)
        while j >= 0 and key < arr[j]:
            # jika nilai j( value : 0) lebih atau sama dengan 0 dan key( value : a) lebih kecil dari arr[j](value : b), dan jika hasil nya true lanjutkan
            # ganti arr[j+1](value : a) menjadi arr[j](value : b)
            arr[j+1] = arr[j]
            j -= 1  # dikarekan butuh index 0, maka nilai j di kurangi 1 maka hasil nya -1
        arr[j+1] = key  # ganti arr[j+1] (value : 0) menjadi key (value: a)


# Data olahan
arr = ['b', 'a', 'c', 'f', 'd', 'e']
print(f'Sebelum di sorting {arr}')
insertionSort(arr)
print(f'Sesudah di sorting {arr}')
