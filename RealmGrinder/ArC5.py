from datetime import timedelta
from math import exp

TARGET = (lambda x: exp((x*0.8)**(2/3)))(390)

def ETA(max_mana, done):
    """Used to calculate Archon Challenge 5 duration.
    Arguments:
    | max_mana : in 1e14
    | done     : in 1e18
    """
    percent = (done*1e18)/TARGET    
    remaining = TARGET - done*1e18
    seconds = timedelta(seconds=int(remaining/(max_mana*1e14)))
    print("{:.2%} done.".format(percent))
    print("Remaining as currently stands:", seconds)
    return seconds
