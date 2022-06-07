def insertionSort(arr):
    for i in range(1, len(arr)):  # menghasilkan 4 putaran
        key = arr[i]  # value : 11 (untuk putara 1)
        j = i-1  # value : 0 (putaran)
        while j >= 0 and key < arr[j]:
            # jika nilai j( value : 0) lebih atau sama dengan 0 dan key( value : 11) lebih kecil dari arr[j](value : 12), dan jika hasil nya true lanjutkan
            # ganti arr[j+1](value : 11) menjadi arr[j](value : 12)
            arr[j+1] = arr[j]
            j -= 1  # dikarekan butuh index 0, maka nilai j di kurangi 1 maka hasil nya -1
        arr[j+1] = key  # ganti arr[j+1] (value : 0) menjadi key (value: 11)


9.  # Data olahan
arr = [12, 11, 13, 5, 6]
print(arr)
insertionSort(arr)
print(arr)
