def fibonacci_search(lst, target):
    size = len(lst)
    start = -1
    f0 = 0
    f1 = 1
    f2 = 1
    while (f2 < size):
        f0 = f1
        f1 = f2
        f2 = f1 + f0
    while (f2 > 1):
        index = min(start + f0, size - 1)
        if lst[index] < target:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif lst[index] > target:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return index
    if (f1) and (lst[size - 1] == target):
        return size - 1
    return None


arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
print(fibonacci_search(arr, 31))
print(fibonacci_search(arr, 35))

'''
algoritma deskriptif
buatlah function fibonacci_search() yang memiliki argument 'list, target', kemudian di dalam function tersebut buatlah beberapa variabel, 'size = len(lst)', 'start = -1', 'f0, fi, f2 = 0, 1, 1' setelah itu lakukan perulangan while do pertama dengan kondisi 'f2 < size' jika hasil nya true maka set nilai variabel 'f0, f1, f2 = f1, f2, f1 + f0'. lakukan while do kedua dengan kondisi 'f2 > 1' jika hasil nya false lakukan pengecekan apakah 'f1 and (lst[seze -1]) == target' jika hasil dari pengecekan tersebut true maka 'return size -1' jika false 'return none', jika hasil dari while kedua tadi true, maka buatlah variabel 'index = min(start + f0, size -1)'
dan lakukan pengecekan, jika 'lst[index] < target' hasil nya true set variabel 'f2, f1, f0, start = f1, f0, f2 - f1, index', jika 'lst[index] > target' set variabel 'f2, f1, f0 = f0, f1 - f0, f2 - f1', dan jika hasil nya false 'return index'
'''
