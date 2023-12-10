#!/usr/bin/env python3

def rab_rec(months: int, offspring : int)-> int:
    """
    Calculate the total number of rabbit pairs after a given number of months.

    Parameters:
    - months (int): The number of months for which to calculate the rabbit population.
    - offspring (int): The number of offspring pairs produced by each reproductive pair.

    Returns:
    - int: The total number of rabbit pairs after the specified number of months.
    """
    
    x = [1,1]
    for i in range(2, months):
     j = x[i-1]+ offspring* x[i-2]
     x.append(j)
    return x[-1]
    

if __name__ == '__main__':
   print(rab_rec(33,3))
   

