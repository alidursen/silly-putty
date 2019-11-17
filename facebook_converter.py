"""
Problem: Facebook, when asked for a copy of personal data, can give JSON records.
However, there's an encode-decode miscommunication in play, they encoded the strings
using UTF-8, but decoded using Latin-1. This script aims to undo that situation.

Usage: Have the script located where your Facebook data folder `facebook-[USERNAME]`
is located and run the command `python3 facebook_converter [USERNAME]`.
Output will be the folder `facebook-[USERNAME]-converted` with original intact.

TODO: Conversion for HTML records, if needed.
"""

import os, pathlib, sys

conv = lambda x: x.encode('latin-1').decode('utf-8')

if __name__ == "__main__":
    if(len(sys.argv) is not 2):
        raise RuntimeError("Needs only 1 additional argument.")
    
    ROOT = './facebook-{}'.format(sys.argv[1])
    CONV_ROOT = ROOT + '-conv'

    for dirpath, subdirnames, filenames in os.walk(ROOT, topdown=False):
        org_path = pathlib.Path(dirpath)
        if(not org_path.exists()):
            raise FileNotFoundError("Folder not found. Is the script on the same folder with your FB data folder?")
        conv_path = pathlib.Path(CONV_ROOT, *(org_path.parts[1:]))
        if(not conv_path.exists()):
            os.makedirs(conv_path)

        for file in filenames:
            if(pathlib.PurePath(file).suffix == '.json'):
                with (org_path/file).open(mode='r', encoding='unicode_escape') as original, (conv_path/file).open(mode='x') as converted:
                    for line in original:
                        try:
                            converted.write(conv(line))
                        except UnicodeDecodeError as e:
                            print(e, line)
                            raise Exception
            else:
                pass
