#!/usr/bin/env python3

# Problem
# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

# The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s
#  then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

# Given: A DNA string s of length at most 1000 bp.

# Return: The reverse complement sc of s

def rev_com(dna_str: str) -> str:
    """
    Generate the reverse complement of a given DNA string.

    Parameters:
    - dna_str (str): The DNA string of length at most 1000 bp.

    Returns:
    str: The reverse complement of the input DNA string.
    """
    dna_str = open(dna_str, "r").read()
    trans_table = str.maketrans("ATGC", "TACG")
    return dna_str.translate(trans_table)[::-1].strip()


if __name__ == '__main__':
    print(rev_com("rosalind_data/rosalind_revc.txt"))