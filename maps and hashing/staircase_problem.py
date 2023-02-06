import time
import seaborn as sns
import matplotlib.pyplot as plt

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

without_caching = []
with_caching    = []

for i in range(31):
    begin = time.time_ns()
    r = staircase(i)
    end = time.time_ns()

    print(f'result {r} with computational time {end-begin}  without caching')
    without_caching.append(end-begin)
    begin = time.time_ns()
    r = staircase_with_caching(i)
    end = time.time_ns()

    print(f'result {r} with computational time {end-begin}  with caching')
    with_caching.append(end-begin)

sns.set_theme()
plt.title('Staircase problem with/without caching')
plt.plot(range(31),without_caching, label='without caching', linestyle='-', color='red')
plt.plot(range(31), with_caching, label='with caching', linestyle='-', color='green')
plt.scatter(range(31),without_caching, color='red')
plt.scatter(range(31),with_caching, color='green')
plt.xlabel('Number of stairs')
plt.ylabel('Time (Nano-seconds)')
plt.xticks(range(31))
plt.legend(labels=['without caching', 'with caching'])

plt.show()