def sorting(array):
    if len(array) <= 1:
        return array
    base = array[len(array)//2]
    less = [x for x in array if x < base]
    equal = [x for x in array if x == base]
    grater = [x for x in array if x > base]
    return sorting(less) + equal + sorting(grater)

array = [int(x) for x in input("Введите элементы массива через пробел:").split()]
print(sorting(array))
