
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(1, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]



# Dividing to parts


def merge_sort(arr, s ,  e):
    if e - s < 2:
        return []

    # divide
    mid = s + (e - s)//2


    merge_sort(arr, s, mid)
    merge_sort(arr, mid, e)
    left_arr    = arr[s:mid]
    right_arr   = arr[mid:e]
    print(f'Dividing: LEFT({left_arr}), RIGHT({right_arr})')

    p = s # start
    s_l = s
    s_r = mid

    while s_l < s + len(left_arr) and s_r < mid + len(right_arr):
        print(f'compare left {left_arr[s - s_l]}  {left_arr} with {right_arr[mid - s_r]} ,,{s_r} ,, right {right_arr}')
        if left_arr[s_l - s] < right_arr[s_r - mid]:
            print(f'pick {left_arr[s_l - s]} from left')
            arr[p] = left_arr[s_l - s]
            s_l+=1
        else:
            print(f'pick {right_arr[s_r - mid]} from right')
            arr[p] = right_arr[s_r - mid]
            s_r+=1
        p+=1

    # add remain elements
    while s_l <  s + len(left_arr):
        print(f'remain: left add {left_arr[s_l - s]}')
        arr[p] = left_arr[s_l- s]
        s_l+=1
        p+=1

    while s_r < mid + len(right_arr):
        print(f'remain: left add {right_arr[s_r - mid]}')
        arr[p] = right_arr[s_r - mid]
        s_r += 1
        p += 1

    print('sorted' ,arr)


print('bubble sort')
arr = [9, 3 ,2 ,6 ,3 ,6, 8, 1, 32, 4]
arr2= [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]

merge_sort(arr, 0, len(arr))
print(arr)
# bubble_sort(arr)
# print(arr)
# bubble_sort(arr2)
# print(arr2)


