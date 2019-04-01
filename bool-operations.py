"""
A restatement of existing `and` and `or` operations.
Note that returned items need not be `bool`-valued.
"""

def OR(x,y):
	if(not x): return y
	else: return x

def AND(x,y):
	if(not x): return x
	else: return y
