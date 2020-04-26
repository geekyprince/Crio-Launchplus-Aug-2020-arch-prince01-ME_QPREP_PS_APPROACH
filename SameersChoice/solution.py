import re
from collections import defaultdict

class Solution:

    #def is_valid_plate_no(self,plateno_valid):

    def lucky_number(self,pattern_list, queries):
        pattern_dict = {}
        print(pattern_list)
        for A in pattern_list:
            l = len(A)
            i=0
            pattern_dict[A[0]] = []
            while(i<l):
                pattern_dict[A[0]] += [[A[1][i],A[1][i]]]
                if(i<l-1):
                    if(A[i+1] == '-'):
                        pattern_dict[A[0]][-1] = [[A[1][i],A[1][i+2]]]
                        i+=2
                i+=1
            #pattern_dict[A[0]] = A[1]
        print(pattern_dict)
