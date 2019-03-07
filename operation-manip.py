from itertools import product as p
from operator import add, mul, sub, truediv, floordiv

"""
Based on brilliant.org question: https://brilliant.org/daily-problems/os-evens-odds/
It asks the user to determine if, using addition, subtraction and multiplication, one can reach
a result of 7 from numbers 2,4,5,3,2 (in that order: since there is subtraction
involved, distinction matters.)

In other words, fill the blanks below using +,- and *:
    2_4_5_3_2 =? 7
"""

def op_manip(l:list=[2,4,5,3,2], target=7, ops:list=[add, mul, sub]):
    for c in p(ops, repeat=len(l)-1):
        r = l[0]
        for i in range(len(c)):
            r = c[i](r,l[i+1])
        if(r==target):
            print("********")
        print(r)
        if(r==target):
            print(*(op.__name__ for op in c))
            print("********")

if __name__=="__main__":
    op_manip()
