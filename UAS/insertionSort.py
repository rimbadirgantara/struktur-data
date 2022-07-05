from os import system as sy
sy('cls')


def iSort(a):
    for i in range(1, len(a)):
        value = a[i]  # 2
        index = i - 1  # 1
        while index >= 0 and value < a[index]:
            a[index + 1] = a[index]
            index -= 1
        a[index + 1] = value


a = [4, 7, 2, 6, 8]
print(f'Data Sebelum di sorting : {a}')
iSort(a)
print(f'Data Sesudah di sorting : {a}')
