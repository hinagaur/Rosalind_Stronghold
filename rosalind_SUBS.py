#!/usr/bin/env python3

def find_motif(DNA_string_1: str, DNA_string_2: str) -> list:
    '''
    Given two DNA strings, DNA_string_1 and DNA_string_2 (each of length at most 1 kbp), this function  returns
    all locations of DNA_string_2  as a substring of DNA_string_1.
    '''
    return [n+1 for n in range(len(DNA_string_1)) if DNA_string_1.find(DNA_string_2 , n) == n]

if __name__ == '__main__':
    print(find_motif('GATATATGCATATACTT', 'ATAT'))
