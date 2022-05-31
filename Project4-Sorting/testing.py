# Data olahan
data = ['a', 'g', 'w', 'z', 'f']
data_ = []
for i in range(len(data)):
    m = min(data)
    data_.append(m)
    data.remove(m)
print(data_)
