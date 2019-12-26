"""Dox4242's save editor at http://dox4242.github.io/edit/edit.html
offers detailed look into various RG stats. However if one wishes to compare
faction or spell times, not much help is given neither in game nor at editor.

These functions (which are in fact identical) take a string as copied from
the editor, compares, prints items in order. Can print descending, can return the list.
"""
from datetime import timedelta as td

def time_comp(s:str, tail:int, reverse:bool=False, detailed:bool=False):
    UNDESIREDS = ["Active Spell Time	",
        "Tax Collection Time	",
        "Hailstorm Time	",
        "Heatwave Time	",
        "Shadow Embrace Time	",
        "Wail of the Banshee Time	",
        "Cannibalize Time	",
        "Unaffiliated Playtime	"
    ]

    s = s.splitlines()
    t = []

    for i in range((len(s)+5)//6):
        if s[6*i] not in UNDESIREDS:
            this_r = td(0)
            for time in s[6*i+3].split():
                unit = time[-1]
                amount = int(time[:-1])
                if(unit=='d'):
                    this_r += td(days=amount)
                if(unit=='h'):
                    this_r += td(hours=amount)
                if(unit=='m'):
                    this_r += td(minutes=amount)
                if(unit=='s'):
                    this_r += td(seconds=amount)
            t.append((s[6*i][:-1], this_r))

    t.sort(key=lambda x: x[1], reverse=reverse)
    for i in t:
        print(i[0][:-1*tail],'\t', str(i[1]))
    if detailed: return t

def faction_time_comp(s:str, reverse:bool=False, detailed:bool=False):
    "Enclose your string in triple quotations."
    return time_comp(s=s, reverse=reverse, tail=9)
def spell_time_comp(s:str, reverse:bool=False, detailed:bool=False):
    "Enclose your string in triple quotations."
    return time_comp(s=s, reverse=reverse, tail=5)
