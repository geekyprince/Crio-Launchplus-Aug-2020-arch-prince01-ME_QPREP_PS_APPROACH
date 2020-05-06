
# Finish this function
Alpha_equivalent_num = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1,27)))

def search_index(car,broken_cars,dist):
    start = 0
    end = len(broken_cars) -1
    while(start <= end):
        mid = start + (end - start)//2
        if(broken_cars[mid] <= car <= broken_cars[mid] + 2 * dist):
            return mid 
        elif(broken_cars[mid] > car):
            end = mid - 1
        else:
            start = mid + 1
    return -1

def find_registration_decode(registration_number):
    #decoding except KA
    first_2_digits = (int(registration_number[2:4]) - 1) * 26 * 26 * 9999 
    first_letter = (Alpha_equivalent_num[registration_number[4]] - 1) * 26 * 9999
    second_letter = (Alpha_equivalent_num[registration_number[4]] - 1) * 9999
    last_4_digits = int(registration_number[-4:]) 

    decoded_registration_number = first_2_digits + first_letter + second_letter + last_4_digits
    return decoded_registration_number


def find_maximum_number_of_people_accomodated(broken, good, dist):
    result = 0
    registration_decode = {}
    broken_cars = []
    good_cars = []
    for car in broken:
        decoded_registration_number = find_registration_decode(car[0])
        registration_decode[decoded_registration_number - dist] = car[1]
        broken_cars.append(decoded_registration_number - dist)
    broken_cars.sort()

    for car in good:
        decoded_registration_number = find_registration_decode(car[0])
        registration_decode[decoded_registration_number] = car[2] - car[1]
        if(broken_cars[0] <= decoded_registration_number <= broken_cars[-1] + dist):
            good_cars.append(decoded_registration_number)
    good_cars.sort()

    for car in good_cars:
        index = search_index(car, broken_cars,dist)
        while(registration_decode[car] and (broken_cars[index] <= car <= broken_cars[index] + 2 * dist)):
            if(registration_decode[broken_cars[index]] > registration_decode[car]):
                registration_decode[broken_cars[index]] -= registration_decode[car]
                result += registration_decode[car]
                registration_decode[car] = 0
                break
            else:
                registration_decode[car] -= registration_decode[broken_cars[index]]
                result += registration_decode[broken_cars[index]]
                registration_decode[broken_cars[index]] = 0
                del broken_cars[index]

    return result
