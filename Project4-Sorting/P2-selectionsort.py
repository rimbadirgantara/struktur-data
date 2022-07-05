# Data olahan
from os import system as sy
sy('cls')
data = [64, 25, 12, 22, 11]
print("Data sebelum diurutkan,")
print(data)
for i in range(len(data)):  # 0 - 4
    min_idx = i  # 0, 1
    for j in range(i + 1, len(data)):  # 1 - 4 -> putaran pertama, 2 - 4 -> putar n kedua
        if data[min_idx] > data[j]:  # 64 > 25 -> True, 64  > 12 - > true
            min_idx = j   # 1, 2
    data[i], data[min_idx] = data[min_idx], data[i]
print("Data sesudah diurutkan,")
print(data)
