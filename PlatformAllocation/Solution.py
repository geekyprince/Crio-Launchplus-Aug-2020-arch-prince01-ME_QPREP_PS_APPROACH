import queue
from heapq import heappush, heappop
from collections import defaultdict

def time_in_milisec(time):
    hour, minutes, sec, milisec = int(time[:2]), int(time[3:5]), int(time[6:8]), int(time[9:])
    return hour * int(3.6e+6) + minutes * int(6e+4) + sec * int(1e+3) + milisec

def allocate(Queue, train_heap):
    plat_heap = []
    all_schedules = defaultdict(list)
    max_platform_required = 0
    while(train_heap):
        train = heappop(train_heap)
        (arrival, departure, num, name) = train

        if(plat_heap and plat_heap[0][0] <= arrival):
            platform = heappop(plat_heap)[1]
        else:
            platform = Queue.pop(0)
            max_platform_required = platform
        
        num = train[2]
        name = train[3]
        departure = train[1]
        all_schedules[num].extend([name, num, platform])
        heappush(plat_heap, (departure, platform))
    
    return max_platform_required, all_schedules

        
        

def get_train_allocations(trains):
    num_trains = len(trains)
    Queue = list(range(1, num_trains + 1))
    train_heap = []

    for name, num, arrival, depart, depart_time_taken in trains:
        arrival = time_in_milisec(arrival)
        departure = time_in_milisec(depart) + time_in_milisec(depart_time_taken)
        train = (arrival, departure, int(num), name)
        heappush(train_heap, train)
    
    max_platform_required, all_schedules = allocate(Queue, train_heap)

    return max_platform_required, all_schedules
