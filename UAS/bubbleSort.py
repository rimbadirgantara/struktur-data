from os import system as sy
sy('cls')


def bsort(a):
    for i in range(len(a) - 1, 0, -1):
        for n in range(i):
            if a[n] > a[n + 1]:
                a[n], a[n+1] = a[n+1], a[n]


a = [6, 3, 8, 4, 6, 5]
print(f'Data sebelum di sorting : {a}')
bsort(a)
print(f'Data sesudah id sorting : {a}')
