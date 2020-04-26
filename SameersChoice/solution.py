import re
from collections import defaultdict

class Solution:
    def is_palindrome(self,n):
        if(n == n[::-1]):
            return True
        return False
    def check_print_number(self,n,vehicle_type,pattern_dict):
        number = ''
        flag = 1  #decide if number is good or bad
        for i in range(4):
            #print('*',pattern_dict[vehicle_type][i][0],int(n[i]),pattern_dict[vehicle_type][i][1])
            if pattern_dict[vehicle_type][i][0] <= int(n[i]) <= pattern_dict[vehicle_type][i][1]: #if 10000 <= number <= 30000:
                number +=  n[i]
            else:
                flag = 0
                number += str(pattern_dict[vehicle_type][i][0])
        if(flag):
            print('Yes','Good')
            return self.is_palindrome(n)
        else:
            print('Yes','Bad',number)
            return False

    def divide_in_four(self, plate_no):
        A = ''
        N = plate_no[-4:]
        S = plate_no[:2]
        if(plate_no[2]=='-'):
            D = plate_no[3:5]
            i = 5
        else:
            D = plate_no[2:4]
            i = 4
        if(plate_no[i]=='-'):
            A += plate_no[i+1:-5]
        else:
            A += plate_no[i:-4]
        return S,D,A,N
        
    def is_valid_plate_no(self,plate_no,state_codes):
        A = plate_no.replace('-', '')
        if(len(A)<8 or len(A)>11):
            return False
        try:
            S,D,A,N = self.divide_in_four(plate_no)
            #print(S,D,A,N)
            if(not N.isnumeric()):
                return False 
            if(not(0<int(D)<99)):
                return False
            if(len(A)>3 and not A.isalpha()):
                return False
            if(S not in state_codes):
                return False
        except:
            return False
        return True
        



            
        

    def lucky_number(self,pattern_list, queries):
        state_codes = ["AP","AS","AR","BR","CG","GA","GJ","HR","HP","JK","JH","KA","KL","MP","MH","ML","MN","MZ","NL","OD","PB","RJ","SK","TN","TS","TR","UK","UP","WB","AN","CH","DD","DL","LA","LD","PY"]
        pattern_dict = {}
        pattern_dict['default'] = [[0, 9], [0, 9], [0, 9], [0, 9]]
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
                        pattern_dict[A[0]][-1] = [int(A[1][i]),int(A[1][i+2])]
                        i+=2
                i+=1
        #print(pattern_dict)
        for A in queries:
            #print(s.replace('a', ''))

            plate_no = A[0]
            if(self.is_valid_plate_no(plate_no,state_codes)):
                if A[1] in pattern_dict.keys():
                    vehicle_type = A[1]
                else:
                    #print('*')
                    vehicle_type = 'default'
                if(self.check_print_number(plate_no[-4:],vehicle_type,pattern_dict)):
                    result += [A]
            else:
                print('No')
        print(len(result))
        for A in result:
            print(*A)
        
        #print(queries)
