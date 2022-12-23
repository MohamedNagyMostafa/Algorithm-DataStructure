import time

caching = {}

def staircase(n):

    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        ways = 0
        ways += staircase(n - 1)
        ways += staircase(n - 2)
        ways += staircase(n - 3)

        return ways

def staircase_with_caching(n):
    if n in caching:
        return caching[n]

    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        ways = 0
        ways += staircase_with_caching(n - 1)
        ways += staircase_with_caching(n - 2)
        ways += staircase_with_caching(n - 3)
        caching[n] = ways

        return ways

begin = time.time_ns()
r = staircase(20)
end = time.time_ns()

print(f'result {r} with computational time {end-begin}  without caching')

begin = time.time_ns()
r = staircase_with_caching(20)
end = time.time_ns()

print(f'result {r} with computational time {end-begin}  with caching')

