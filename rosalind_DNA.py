#!/usr/bin/env python3

def count_nt(dna_string: str) -> str:
    """
    Counts the occurrences of nucleotides (A, T, G, C) in a given DNA string.

    Parameters:
    - dna_string (str): The DNA string of length at most 1000 nt.

    Returns:
    str: A formatted string containing the counts of each nucleotide (A, C, G, T).
    """
    file= open(dna_string, "r").read()
    return f'{file.count("A")} {file.count("C")} {file.count("G")} {file.count("T")}'

if __name__ == '__main__':
    count = count_nt("rosalind_data/rosalind_dna.txt")
    print(count)
