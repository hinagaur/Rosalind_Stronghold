#!/usr/bin/env python3

def dom_prcnt(hom_dom_no: int, het_no: int, hom_rec_no: int,)-> float:
    """
    Calculates the probability that two randomly selected mating organisms will produce an individual possessing a 
              dominant allele

    Args:
       hom_dom_no(int): Number of individuals with homozygous dominant genotype (DD).
        het_no (int): Number of individuals with heterozygous genotype (Dd).
        hom_rec_no (int): Number of individuals with homozygous recessive genotype (dd).

    Returns:
        float: The probability that two randomly selected mating organisms will produce an individual possessing a 
              dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
    """
    hom_dom = 'DD'
    hom_rec = 'dd'
    het = 'Dd'

    #Initializing a list containing all the homozygous dominant(DD), heterozygous(dD), and homozygous recessive(dd)
    # individuals for a trait
    list_1 = []
    for _ in range(hom_dom_no):
       list_1.append(hom_dom)

    for _ in range(hom_rec_no):
       list_1.append(hom_rec)

    for _ in range(het_no):
        list_1.append(het)
    
    #Initializing a list contating all the possible matches between the individuals in list_1
    list_2 = []

    for i in range(len(list_1)):
        for j in range(i+1, (len(list_1))):
            list_2.append([list_1[i],list_1[j]])
    
    #List containing all the possible zygosity of the offsprings
    list_3 = []

    for k in list_2:
        for l in k[0]:   
            for m in k[1]:
                list_3.append(f'{l}{m}')

    #Counting the individuals with dominant and non-dominant phenotype of that trait
    count_dom = 0
    count_non_dom = 0

    for i in list_3:
        if i == 'DD' or i == 'Dd' or i == "dD":
            count_dom +=1
        else:
            count_non_dom +=1

    percentage = count_dom / (count_dom+count_non_dom)
    return round(percentage,5)

if __name__ == '__main__':
    print(dom_prcnt(29 ,21 ,26))

