def power_of_2(n):
    if n <= 0:
        return 1
    return 2 * power_of_2(n-1)

def sum_of_integers(n):
    if n <= 0:
        return 0
    else:
        return n + sum_of_integers(n - 1)

def sum_of_arr(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_of_arr(arr[1:])

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial( n - 1)

def reverse_string(string):
    if len(string) == 0:
        return ""
    return string[-1] + reverse_string(string[:-1])

def is_palindrome(text):
    if len(text) <= 1:
        return True
    l = text[0]
    r = text[-1]
    if l != r:
        return False
    return is_palindrome(text[1:-1])

print(is_palindrome('madam'))