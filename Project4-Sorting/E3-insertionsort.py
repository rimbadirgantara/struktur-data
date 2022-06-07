def a(a):
    for i in range(1, len(a)):
        # menghasil kan 5 x putaran
        key = a[i]  # ambil nilai index dari nilai i
        a_ = a - 1
        while a_ >= 0 and key < a[a_]:
            a[a_+1] = a[a_]
            a_ -= 1
        a[a_+1] = a[key]


a = ['b', 'a', 'c', 'f', 'd', 'e']
print(f'data awal : {a}')
a(a)
print(f'setelah di sorting : {a}')
