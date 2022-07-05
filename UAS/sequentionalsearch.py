from os import system as sy
sy('cls')


def sequentionalSearch(search, a):
    index = 0
    ketemu = False
    while index >= 0 and not ketemu:
        if a[index] == search:
            ketemu = True
        else:
            index += 1
    return f'Data {search} berada di index {index}'


a = [4, 7, 2, 8, 3]
search = int(input(f'{a}\nSearch ? '))
print(sequentionalSearch(search, a))
