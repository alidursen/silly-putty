"""
Problem: Facebook, when asked for a copy of personal data, can give JSON records.
However, there's an encode-decode miscommunication in play, they encoded the strings
using UTF-8, but decoded using Latin-1. This script aims to undo that situation.

Usage: Have the script located where your Facebook data folder `facebook-[USERNAME]`
is located and run the command `python3 facebook_converter [USERNAME]`.
Output will be the folder `facebook-[USERNAME]-converted` with original intact.

TODO: * Conversion for HTML records, if needed.
      * Complete copying, or changing in-place options.

Current problem and vector of solution:
    https://docs.python.org/3/howto/unicode.html#reading-and-writing-unicode-data
We instead went with `unicoded` method.
"""

import os, pathlib, sys

conv = lambda x: x.encode('latin-1').decode('utf-8')
def unicoded(s:str)->str:
    """
    Recursively finds the first occurance of \\u and either corrects or
    keeps it. Decision is based on amount of backslashes: if the printed
    version has even, then they are all escape-character sequences.

    On very long lines, recursion limits occur. Reverting to loop-based solution.
    """
    def counter(i:int)->bool:
        """If, right before s[i] (which will be a start index for \\u)
        there're an odd number of \\, ie. u is not escaped, will return False,
        indicating that we should move on.
        """
        count = True
        for ch in s[i-1::-1]:
            if(ch=='\\'): count = not count
            else: break
        return count

    # We can't use `replace` because as unlikely as it may be,
    # there's no guarantee that we didn't write an unicode in original
    # file. Therefore escape-counting is always needed.
    t_loc = 0
    loc = s.find('\\u')
    corrected = ''
    while(loc>0):
        corrected += s[t_loc:loc]
        if(counter(loc)):
            t_loc = loc + 6
            corrected += eval("'{}'".format(s[loc:t_loc]))
        else:
            t_loc = loc + 2
            corrected += s[loc:t_loc]
        loc = s.find('\\u', t_loc)
    corrected += s[t_loc:]
    return corrected

if __name__ == "__main__":
    if(len(sys.argv) is not 2):
        raise RuntimeError("Needs exactly 1 additional argument.")
    
    ROOT = './facebook-{}'.format(sys.argv[1])
    CONV_ROOT = ROOT + '-conv'

    if(not pathlib.Path(ROOT).exists()):
        raise FileNotFoundError("Folder not found. Is the script on the same folder with your FB data folder?")

    for dirpath, subdirnames, filenames in os.walk(ROOT, topdown=False):
        org_path = pathlib.Path(dirpath)
        conv_path = pathlib.Path(CONV_ROOT, *(org_path.parts[1:]))
        if(not conv_path.exists()):
            os.makedirs(conv_path)

        for file in filenames:
            if(pathlib.PurePath(file).suffix == '.json'):
                # There's a problem: somehow, `encoding='unicode_escape'` does not
                # work as intended and (specifically) comments.json throw unicode error.
                # This is **not** due to there being a phrase organically containing
                # '\u' in it: all occurences of '\u' occur within context of unicodes.
                # Furthermore, function as it were **did** work on other files.
                # 
                # A solution: since copying and pasting json's work, let Python
                # read them as they are: use `eval` for manual unicode_escape.
                #  
                # with (org_path/file).open(mode='r', encoding='unicode_escape') as original, (conv_path/file).open(mode='x') as converted:
                with (org_path/file).open(mode='r') as original, (conv_path/file).open(mode='x') as converted:
                    for line in original:
                        try:
                            converted.write(conv(unicoded(line)) if '\\u' in line else line)
                        except Exception as e:
                            print('='*32+"\nProblem at file:", (org_path/file))
                            print("        at line:", line, '\n'+'='*32)
                            raise e
            else:
                pass
