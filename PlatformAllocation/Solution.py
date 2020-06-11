import queue
from heapq import heappush, heappop
from collections import defaultdict

def time_in_milisec(time):
    hour, minutes, sec, milisec = int(time[:2]), int(time[3:5]), int(time[6:8]), int(time[9:])
    return hour * int(3.6e+6) + minutes * int(6e+4) + sec * int(1e+3) + milisec

def allocate(train_heap):
    plat_heap = []
    departure_heap = []
    all_schedules = defaultdict(list)
    max_platform_required = 0
    while(train_heap):
        train = heappop(train_heap)
        (arrival, departure, num, name) = train

        while(departure_heap and departure_heap[0][0] <= arrival):
            platform = heappop(departure_heap)[1]
            heappush(plat_heap, platform)
        if(plat_heap):
            platform = heappop(plat_heap)
        else:
            max_platform_required += 1
            platform = max_platform_required
        num = train[2]
        name = train[3]
        departure = train[1]
        all_schedules[num].extend([name, num, platform])
        heappush(departure_heap, (departure, platform))
    
    return max_platform_required, all_schedules

        
        

def get_train_allocations(trains):
    num_trains = len(trains)
    train_heap = []

    for name, num, arrival, depart, depart_time_taken in trains:
        arrival = time_in_milisec(arrival)
        departure = time_in_milisec(depart) + time_in_milisec(depart_time_taken)
        train = (arrival, departure, int(num), name)
        heappush(train_heap, train)
    
    max_platform_required, all_schedules = allocate(train_heap)

    return max_platform_required, all_schedules
