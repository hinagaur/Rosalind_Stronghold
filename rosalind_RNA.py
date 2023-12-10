#!/usr/bin/env python3

def DnatoRna(nucleic_acid : str) -> str:
    """
    This function converts DNA to RNA.
    """
    nucleicAcid= open(nucleic_acid, "r").read()
    RNA= nucleicAcid.replace("T","U").strip()
    return RNA

if __name__ == '__main__':
    comp= DnatoRna("rosalind_data/rosalind_rna.txt")
    print(comp)