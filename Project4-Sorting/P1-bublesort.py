# Membuat method buble sort

def bubblesort(elements):  # def adalah syntax untuk membuat funciton / method
    # for bagian awal digunakan untuk stetament perulangan
    for n in range(len(elements) - 1, 0, -1):
        for i in range(n):  # for bagian kedua digunakan sebagai index dari var elements
            if elements[i] > elements[i + 1]:  # membandingkan index var element
                # mereplace index elements sesuai nilai index dari hasil for
                elements[i], elements[i + 1] = elements[i + 1], elements[i]

 # data olahan dalam bentuk list
elements = [39, 12, 18, 85, 72, 10, 2, 18]
print("Data sebelum diurutkan,")
print(elements)
bubblesort(elements)
print("Data sesudah diurutkan, ")
print(elements)
