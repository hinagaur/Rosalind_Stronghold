#!/usr/bin/env python3

gen_1= ['AA','AA']
gen_2= ['AA','Aa']
gen_3=['AA','aa']
gen_4=['Aa','Aa']
gen_5=['Aa','aa']
gen_6= ['aa','aa']


def dom_prob(genotype:list, num:int)-> float:
    ''' This function takes in the genotype pairing for a given factor for a couple as a list and the number of couples and returns the probability
    of having an offspring with dominant phenotype if each couple produces two offsprings.'''

    if num == 0:
        return 0
    else:
        a=0
        gen_list_1 = []

        while a < num:
            for i in genotype[0]:
                for j in genotype[1]:
                    gen_list_1.append(i+j)
            a +=1

        dom = 0
        rec = 0

        for k in gen_list_1:
            result= "A" in k
            if result == True:
                 dom+=1
            else:
                 rec+=1

    prob = (dom / len(gen_list_1)) * 2
    return prob
    

# if __name__ == '__main__':
#     print(dom_prob(gen_1,0))

gen_list = [gen_1, gen_2, gen_3, gen_4, gen_5, gen_6]

population = open("rosalind_data/rosalind_iev.txt", "r").read()
number= population.strip().split(" ")


total_prob = 0
for l,m in zip(gen_list, number):
    prob = dom_prob(l,int(m))
    # print(prob)
    total_prob += prob

print(total_prob)

# f = open("rosalind_data/rosalind_iev.txt", "r")
# f = f.readline()
# b = f.split(" ")
# bint = []
# for i in range (0, len(b)):
#     bint.append(int(b[i]))

# def expected (a):
#     sum = (a[0] * 1 + a[1] * 1 + a[2] * 1 + a[3] *0.75 + a[4] *0.5 + a[5] * 0) * 2
#     return sum

# print(expected(bint))
