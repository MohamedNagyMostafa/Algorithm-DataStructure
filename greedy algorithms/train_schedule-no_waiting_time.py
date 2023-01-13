from queue import PriorityQueue

class Train:

    def __init__(self, dep_time, arr_time):
        self.dep_time = dep_time
        self.arr_time = arr_time

    def __le__(self, other):
        return self.dep_time <= other.dep_time

    def __ge__(self, other):
        return self.dep_time >= other.dep_time

    def __gt__(self, other):
        return self.dep_time > other.dep_time

    def __lt__(self, other):
        return self.dep_time < other.dep_time

class Platform:

    def __init__(self, busy_time):
        self.busy_time = busy_time

    def __le__(self, other):
        return self.busy_time <= other.busy_time

    def __ge__(self, other):
        return self.busy_time >= other.busy_time

    def __lt__(self, other):
        return self.busy_time < other.busy_time

    def __gt__(self, other):
        return self.busy_time > other.busy_time

def min_platforms(arrivals, departures):
    # Add trains
    trainsQueue             = PriorityQueue()
    runningPlatformsQueue   = PriorityQueue()

    available_platforms = []
    num_platforms       = 0

    [trainsQueue.put(Train(dep_time= dep_time, arr_time= arr_time)) for dep_time, arr_time in zip(departures, arrivals)]

    while not trainsQueue.empty():
        next_train = trainsQueue.get()
        print('Next train: ', next_train.dep_time)
        # Add retrieve free platforms
        print('release available platforms!')
        if not runningPlatformsQueue.empty():
            top_platform = runningPlatformsQueue.get()
            while top_platform.busy_time <= next_train.dep_time:
                print('found a platform to clear', top_platform.busy_time)
                available_platforms.append(top_platform)

                if runningPlatformsQueue.empty():
                    break

                top_platform = runningPlatformsQueue.get()
            else:
                runningPlatformsQueue.put(top_platform)

        print('launch the train')
        # Launch trains
        if len(available_platforms) < 1:
            print('create a new platform')
            platform = Platform(busy_time= next_train.arr_time)
            num_platforms += 1
            runningPlatformsQueue.put(platform)
        else:
            print('use a pre-platform')
            platform = available_platforms.pop()
            platform.busy_time = next_train.arr_time

            runningPlatformsQueue.put(platform)
        print('number of stations is: ', num_platforms)
    return num_platforms

# Case 1
departure   = [900,  940, 950,  1100, 1500, 1800]
arrival     = [910, 1200, 1120, 1130, 1900, 2000]

needed_platforms = min_platforms(arrivals= arrival, departures= departure)
assert needed_platforms == 3

print(f'Number of needed platforms are: {min_platforms(arrivals= arrival, departures= departure)}')

print('= ================= break =================')
# Case 2
departure   = [200, 210, 300, 320, 350, 500]
arrival     = [230, 340, 320, 430, 400, 520]

needed_platforms = min_platforms(arrivals= arrival, departures= departure)
assert needed_platforms == 2

print(f'Number of needed platforms are: {min_platforms(arrivals= arrival, departures= departure)}')