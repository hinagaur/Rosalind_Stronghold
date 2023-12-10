#!/usr/bin/env python3

# Fuction to remove empty strings from a list
def rem_empty(test_list: list) -> list:
    '''This function removes empty values from a list instance.'''
    return [i for i in test_list if len(i) > 0]

def gc_count(fasta_file:str)-> int:
    """
    Identify the DNA string in FASTA format with the highest GC-content.

    Parameters:
    - fasta_strings (str): A string containing at most 10 DNA strings in FASTA format.

    Returns:
    Str: The ID of the string with the highest GC-content and the corresponding GC-content.
    """
    contents= open(fasta_file, "r").read()

    #Stripping trailing new lines, splitting it by a ">", and removing empty values
    seqs = contents.strip().split(">")
    seqs = rem_empty(seqs)

    # Looping through each sequence in the FASTA file 
    gc_list = []
    for i in seqs:
         seqfa = i.strip().split("\n")
         header = seqfa[0]
         seq = "".join(seqfa[1:])
         gc_count = (seq.count("G") + seq.count("C")) / len(seq) * 100
         gc_list.append(gc_count)

    
    # Getting the highest percentage of GC content
    highest_gc = max(gc_list)   

    #Prining the ID and GC% of the sequence with highest GC%
    for i in seqs:
        seqfa = i.strip().split("\n")
        header = seqfa[0]
        seq = "".join(seqfa[1:])
        gc_count = (seq.count("G") + seq.count("C")) / len(seq) * 100
        if gc_count == highest_gc:
             return f'{header}\n{round(gc_count, 6)}'
    
    
if __name__ == '__main__':
    print(gc_count("rosalind_data/rosalind_gc.txt"))

    

   








