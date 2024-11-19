"""Пузырьковая сортировка"""
print(__doc__)
def bubble_sort(array):
    n = len(array)
    for nums in range(n):
        swapped = False
        for i in range(0, n - nums - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        if not swapped:
            break
    return array

print(bubble_sort([1000, 2321, 23, 233,224]))

print('-------------------------')

doc = """Двоичный поиск"""
print(doc)
N = list(range(1,5000))
def binary_search(number,array):
    First = 0
    Last = len(array) - 1
    ResultOk = False

    while First < Last:
        Middle = (First + Last) // 2
        if array[Middle] == number:
            ResultOk = True
            pos = array[Middle]
            return (ResultOk, pos)
        elif array[Middle] < number:
            First = Middle + 1
        elif array[Middle] > number:
            Last = Middle - 1

    return ResultOk



answer=binary_search(7,N)
if True in answer:
    print('Элемент найден - '+str(answer[1]))
else:
    print('Элемент не найден')

