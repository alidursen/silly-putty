"""
A restatement of existing `and` and `or` operations.

Also included is an equivalent of `var1 if cond else var2`
expression. Though that expression by itself is easily
comprehensible, its similarities with `and/or` warrant
it a place here.

Note that returned items need not be `bool`-valued.
Also note that, since OR(x,y) is different than OR(y,x),
this also means `x or y` is different than `y or x`
(and vice versa for `and`.)
"""

def OR(x,y):
	if(x): return x
	else: return y

def AND(x,y):
	if(x): return y
	else: return x

def IF_ELSE(var1, var2, cond):
        if(cond): return var1
        else: return var2
