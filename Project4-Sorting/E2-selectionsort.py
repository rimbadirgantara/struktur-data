# Data olahan
# var untuk menampung data yang akan di sorting
data = ['b', 'a', 'c', 'f', 'd', 'e']
print(f'Data Sebelum diurutkan \n{data}')
data_ = []  # var untuk menampung data yang sudah di sorting
for i in range(len(data)):  # for sebanyak var data
    m = min(data)  # mencari nilai terkecil di var data
    # setelah mendapatkan nilai terkecil lalu di masukkan ke dalam var data_
    data_.append(m)
    data.remove(m)  # hapus nilai yang sudah di masukkan ke var dat_
del data, m  # hapus variabel
print(f'Data sesudah diurutkan\n{data_}')  # tampilkan hasil
