"""
A classic measurement problem: when you have 6 items, of which 1 weighs different,
find the different one in minimum measurements.

Inspired by: https://brilliant.org/daily-problems/which-one-different/
"""
from random import randrange

def one_variant(n):
    """
    Creates a list of length n, with all elements c same in range 5<=c<15,
    then changes a random one 1 up or down at random.
    """
    c = randrange(5,15)
    arr = list(c for i in range(n))
    arr[randrange(0,n)] += (-1)**randrange(0,2)
    return arr

def solver6(arr)->bool:
    """
    Solves the stated problem for an array of length 6, in at most 3 measurements.

    Keep in mind that `ìf(c)` conditional is entered if c is non-zero.
    """
    if(len(arr) != 6):
        print("not of length 6")
        return False
    c1 = arr[0]+arr[1]-arr[2]-arr[3]
    if(c1):
        c2 = arr[0]+arr[2]-arr[1]-arr[3]
        m = (c1+c2)/2
        if(m==0):
            c3 = arr[0]-arr[1]
            if(c3 == 0): claim = 2
            else: claim = 1
        else:
            c3 = arr[0]-arr[1]
            if(c3 == 0): claim = 3
            else: claim = 0
    else:
        c2 = arr[0]-arr[4]
        if(c2): claim = 4
        else: claim = 5

    base = arr[claim-1]
    for i in range(6):
        arr[i] -= base
    if(not arr[claim]): print("Error: non-zero is guessed to be",
                    claim, "whereas array is", arr)
    return bool(arr[claim])
