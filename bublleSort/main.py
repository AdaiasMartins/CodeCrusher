list = [0, 1, 5, 3, 4, 5, 6, 7, 8, 9]

def bublleSort(array):
    n = len(array)
    for i in range(0, n-1, +1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]


bublleSort(list)
print(list)