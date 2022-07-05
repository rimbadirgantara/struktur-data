def fibonacci_search(lst, target):
    size = len(lst)
    start = -1
    f0 = 0
    f1 = 1
    f2 = 1
    while (f2 < size):
        f0 = f1
        f1 = f2
        f2 = f1 + f0
    while (f2 > 1):
        index = min(start + f0, size - 1)
        if lst[index] < target:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif lst[index] > target:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return index
    if (f1) and (lst[size - 1] == target):
        return size - 1
    return None


arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
a = int(input(f'Data : {arr}\nSearch ? '))
print(fibonacci_search(arr, a))
