"""Dox4242's save editor at http://dox4242.github.io/edit/edit.html
offers detailed look into various RG stats. However if one wishes to compare
faction or spell times, not much help is given neither in game nor at editor.

These functions (which are in fact identical) take a string as copied from
the editor, compares, prints items in order. Can print descending, can return the list.
"""
from datetime import timedelta as td
import base64, zlib

def save_read(save:str):
    # We can run RegEx's from codec but they're simple enough for a direct check
    # 'struct': /^\$([0-9]{2})s(.*)\$e$/,
    # 'sol': /^\$s0(.*)\$e([0-9]+)$/,
    # 'json': /^\$s(.*)\$e$/,
    conds = {
        'struct': lambda s: (
            s[0]==s[-2]=='$' and
            s[1:3].isdigit() and
            s[3]=='s' and
            s[-1]=='e'
        ),
        'sol': lambda s: (
            s[0]=='$' and
            s[1]=='s' and
            s[2]=='0' and
            s[s.rindex('$')+1]=='e' and
            s[s.rindex('$')+2:].isdigit()
        ),
        'json': lambda s: (
            s[0]==s[-2]=='$' and
            s[1]=='s' and
            s[-1]=='e'
        )
    }

    seperators = {
        'struct': lambda s: (s[1:3],s[4:-2]),
        'sol': DeprecationWarning,
        'json': DeprecationWarning,
    }

    vigenere = lambda e, key: bytes([e[i]^key[i%len(key)] for i in range(len(e))])

    # Item of interest is parantheses part: (.*) is save itself,
    # on struct or sol there's also ([0-9]) which is version.
    for cond in conds:
        if(conds[cond](save)):
            break
    else:
        raise Exception("Unknown save format")

    if(cond=='struct'):
        # Extract pure save string
        ver, save = seperators[cond](save)
        # Decode into bytes using Base64 scheme
        save = base64.b64decode(save)
        # Deflate data, so that save is at this point a bytes object
        # In Python, `bytes` are immutable
        save = zlib.decompress(save)
        save = vigenere(save, b'therealmisalie')
    else: raise seperators[cond]

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
            t.append([s[6*i][:-1], this_r])

    t.sort(key=lambda x: x[1], reverse=reverse)
    if not detailed:
        t = [t[0]]+[[i[0],i[1]-t[0][1]] for i in t[1:]]
    for i in t:
        print(i[0][:-1*tail],'\t', ('' if detailed else '+')+str(i[1]))
    if detailed: return t

def faction_time_comp(s:str, reverse:bool=False, detailed:bool=False):
    "Enclose your string in triple quotations."
    return time_comp(s=s, reverse=reverse, tail=9, detailed=detailed)
def spell_time_comp(s:str, reverse:bool=False, detailed:bool=False):
    "Enclose your string in triple quotations."
    return time_comp(s=s, reverse=reverse, tail=5, detailed=detailed)
