# Data olahan
data = [64, 25, 12, 22, 11]
print("Data sebelum diurutkan,")
print(data)
for i in range(len(data)):
    min_idx = i
    for j in range(i + 1, len(data)):
        if data[min_idx] > data[j]:
            min_idx = j
    data[i], data[min_idx] = data[min_idx], data[i]
print("Data sesudah diurutkan,")
print(data)
