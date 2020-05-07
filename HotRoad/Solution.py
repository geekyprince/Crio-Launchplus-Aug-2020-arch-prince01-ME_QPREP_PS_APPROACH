
# Finish this function
Alpha_equivalent_num = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1,27)))

def decode_registration_num(registration_number):
    #decoding except KA
    first_2_digits = (int(registration_number[2:4]) - 1) * 26 * 26 * 9999 
    first_letter = (Alpha_equivalent_num[registration_number[4]] - 1) * 26 * 9999
    second_letter = (Alpha_equivalent_num[registration_number[4]] - 1) * 9999
    last_4_digits = int(registration_number[-4:]) 

    decoded_registration_number = first_2_digits + first_letter + second_letter + last_4_digits
    return decoded_registration_number


def find_maximum_number_of_people_accomodated(broken, good, dist):
    result = 0
    good_car_list = []
    bad_car_list = []
    Car_bad_Dict = {}
    Car_good_Dict = {}
    for car in broken:
        registration_num = decode_registration_num(car[0])
        #print(car[0],registration_num)
        Car_bad_Dict[registration_num - dist] = car[1]   #people in broken car
        bad_car_list.append(registration_num - dist)
    
    bad_car_list.sort()
    broken = bad_car_list

    for car in good:
        registration_num = decode_registration_num(car[0])
        Car_good_Dict[registration_num] = car[2] - car[1]   #remaining capacity of good car
        good_car_list.append(registration_num)
    
    good_car_list.sort()
    good = good_car_list
    num_broken = len(broken)  
    j = 0    #index for broken
    for car in good:
        while(Car_good_Dict[car] and j < num_broken):
            if(broken[j] <= car <= broken[j] + 2 * dist):
                if(Car_bad_Dict[broken[j]] <= Car_good_Dict[car] ):
                    result += Car_bad_Dict[broken[j]]
                    Car_good_Dict[car] -= Car_bad_Dict[broken[j]]
                    Car_bad_Dict[broken[j]]
                    j += 1
                else:
                    result += Car_good_Dict[car]
                    Car_bad_Dict[broken[j]] -= Car_good_Dict[car]
                    Car_good_Dict[car] = 0
            else:
                j += 1
    print(Car_good_Dict, Car_bad_Dict)
    return result
