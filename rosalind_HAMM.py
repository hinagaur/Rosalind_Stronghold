#!/usr/bin/env python3


def hamm_count(DNA_strings: str)-> int:
    '''
    Given two strings s and t of equal length, this function calculates thethe Hamming distance between s and t denoted dH(s,t)
    s the number of corresponding symbols that differ in s and t.

    - Parameters:
    DNA_strings (str): Inclusdes two DNA strings separated by a new line character

    Returns:
    int : The number of corresponding symbols that differ in s and t.
    '''
    contents = open(DNA_strings, "r").read()
    strings = contents.strip().split("\n")
    s_s = strings[0]
    s_t = strings[1]
    x = 0
    for i,j in zip(s_s, s_t):
        if i !=j:
          x += 1
    return(x)


if __name__ == '__main__':
   print(hamm_count("rosalind_data/rosalind_hamm.txt"))