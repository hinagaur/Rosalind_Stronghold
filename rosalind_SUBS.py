#!/usr/bin/env python3

# s = 'GATATATGCATATACTT'
# t= 'ATAT'

def substr(s: str, t: str) -> list:
    ''' Given two DNA strings s and t (each of length at most 1 kbp), this function return all locations of t as a substring of s.
    '''
    my_list = []
    for i in range(len(s)):
        if s[i:].startswith(t):
            my_list.append(i+1)
    return my_list

if __name__ == '__main__':
    s = 'GATATATGCATATACTT'
    t= 'ATAT'
    print(substr(s,t))



    