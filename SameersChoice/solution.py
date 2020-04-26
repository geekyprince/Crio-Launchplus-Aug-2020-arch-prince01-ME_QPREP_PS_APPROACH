import re
from collections import defaultdict

class Solution:
    def check_print_number(self,n,vehicle_type,pattern_dict):
        number = ''
        flag = 1  #decide if number is good or bad
        for i in range(4):
            if pattern_dict[vehicle_type][i][0] <= int(n) <= pattern_dict[vehicle_type][i][1]: #if 10000 <= number <= 30000:
                number +=  n
            else:
                flag = 0
                number += str(pattern_dict[vehicle_type][i][0])
        if(flag):
            print('Yes','Good')
            return True
        else:
            print('Yes','Bad',number)
            return False

    def is_valid_plate_no(self,plate_no,state_codes):
        l = len(plate_no)
        if(l<8 or l>11):
            return False
        try:
            if plate_no[0:2] not in state_codes:            #checking State code
                return False
            for i in plate_no[2:4]:                         #checking District code
                i = int(i)       #may lead to exception
                if(i<0 or i>9):
                    return False 
            x = l-8
            if(x>3 or not plate_no[4:4+x].isalpha()):      #checking presence of alphabet one two three or none
                return False 
            if(not l[-4:].isnumeric()): #and  l[-4:]!= l[-4:][::-1]):  #checking Palindrome
                return False
        except:
            return False
        return True
            
        

    def lucky_number(self,pattern_list, queries):
        state_codes = ["AP","AS","AR","BR","CG","GA","GJ","HR","HP","JK","JH","KA","KL","MP","MH","ML","MN","MZ","NL","OD","PB","RJ","SK","TN","TS","TR","UK","UP","WB","AN","CH","DD","DL","LA","LD","PY"]
        pattern_dict = {}
        result = []
        #print(pattern_list)
        for A in pattern_list:
            l = len(A[1])
            i=0
            pattern_dict[A[0]] = []
            while(i<l):
                pattern_dict[A[0]] += [[int(A[1][i]),int(A[1][i])]]
                if(i<l-1):
                    if(A[1][i+1] == '-'):
                        pattern_dict[A[0]][-1] = [[int(A[1][i]),int(A[1][i+2])]]
                        i+=2
                i+=1
        for A in queries:
            #print(s.replace('a', ''))
            A[0] = A[0].replace('-','')
            if(self.is_valid_plate_no(A[0],state_codes)):
                vehicle_type = A[1]
                if(self.check_print_number(l[-4:],vehicle_type,pattern_dict)):
                    result += [A]
            else:
                print('No')
        for A in result:
            print(*A)
        
        #print(queries)
