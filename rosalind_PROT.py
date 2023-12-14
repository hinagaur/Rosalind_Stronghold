#!/usr/bin/env python3

#Making a dictionary 
codon_table = {
    "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}


def RnaToProt(mrna: str)-> str:
    '''Translate an mRNA sequence into a protein sequence.

    Args:
        file_path (str): The path to a text file containing the mRNA sequence.

    Returns:
        str: The translated protein sequence.
    '''
    
    #Opening the file containing the mrna sequence
    mrna_seq = open(mrna, "r").read().strip()

    #Making a list of all the three letter codons in the sequence
    codon_list = []
    for i in range(0, len(mrna_seq), 3):
        codon_list.append(mrna_seq[i:i+3])
    
    prot_str = ""
    for j in codon_list:
        prot_code = codon_table.get(j)
        if j == "UAA" or j == "UAG" or j == "UGA":
            break
        elif prot_code == None:
            pass
        else:
           prot_str += prot_code
    return prot_str
  

if __name__ == '__main__':
    print(RnaToProt("rosalind_data/rosalind_prot.txt"))