from Solution import *


def main():


    #test_pq()
    n = int(input().strip())
    trains = [input().strip().split() for x in range(n)]

    all_train_no = [int(x[1]) for x in trains]
    (max_platform_required, all_schedules) = get_train_allocations(trains)

    print(max_platform_required)
    for train_no in all_train_no:
        sched = all_schedules[train_no]
        print(sched)
        #print("{} {} {}".format(sched[0], sched[1], sched[2]))

main()
