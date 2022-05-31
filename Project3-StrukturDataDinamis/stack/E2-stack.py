from os import system as sy
sy('cls')  # error jika os yang digunakan selain windows


class MyGebetan:

    def __init__(self):
        self.cewe = []

    def push(self, gebetan):
        if gebetan not in self.cewe:
            for i in gebetan:
                self.cewe.append(i)
            return True
        else:
            return False

    def pop(self):
        if len(self.cewe) <= 0:
            return ('tidak ada cewe di daftar')
        else:
            return self.cewe.pop()


print(f'\nTipe class -> {MyGebetan}')

print('\nA. Fasilitas Push')
a = MyGebetan()
calon = ['Asri', 'Lastri', 'Kholivatus', 'Ime', 'Cece Joyce']
print(f'Data yang akan di push -> {calon}\nSebelum di push {a.cewe}')
a.push(calon)
print(f'Sesudah di push {a.cewe}')

print('\nB. Fasilitas Pop')
print(f'Sebelum di pop {a.cewe}')
a.cewe.pop()
print(f'Sesudah di pop {a.cewe}')
