

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

# In case of repeated items
def find_first(array, target):
    index = binary_search(array= array, target= target)
    if index == -1:
        return -1
    while array[index - 1] == target:
        index-=1

    return index

target  = 7
array   =  [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]

print(f'Number {target} in array {array} at index({binary_search(array= array, target= target)})')
print(f'Number {target} in array {array} at first index({find_first(array= array, target= target)})')
