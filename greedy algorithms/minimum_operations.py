
def num_min_operations(target):
    num_operations = 0
    while target > 0:
        if target % 2 != 0:
            target-=1
            num_operations+=1
        else:
            num_operations+=1
            target /= 2

    return num_operations


print(num_min_operations(target=69))