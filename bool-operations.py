"""
A restatement of existing `and` and `or` operations.
Note that returned items need not be `bool`-valued.

Also note that, since OR(x,y) is different than OR(y,x),
this also means `x or y` is different than `y or x`
(and vice versa for `and`.)
"""

def OR(x,y):
	if(not x): return y
	else: return x

def AND(x,y):
	if(not x): return x
	else: return y
