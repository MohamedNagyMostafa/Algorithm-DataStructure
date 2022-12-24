

def binary_search_rec(arr, target , start, end):
    index = start + int((end - start)/2)
    if start > end:
        return -1

    if target > arr[index]:
        return binary_search_rec(arr= arr, target= target, start= index + 1, end= end)
    elif target < arr[index]:
        return binary_search_rec(arr= arr, target= target, start= start, end= index - 1)
    else:
        return index

def binary_search(array, target):
    return binary_search_rec(array, target, start= 0, end= len(array))


target  = 10
array   = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]

print(f'Number {target} in array {array} at index({binary_search(array= array, target= target)})')
