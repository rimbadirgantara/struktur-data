from os import system as sy
sy('cls')


def sSort(a):
    a_ = []
    for i in range(len(a)):
        a__ = min(a)
        a_.append(a__)
        a.remove(a__)
    return a_


a = [4, 7, 2, 6, 8]
print(f'Data sebelum di sorting : {a}')
print(f'Data sesudah di sorting : {sSort(a)}')
