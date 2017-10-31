"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def main():
    resp = nsfg.ReadFemResp()
    preg = nsfg.ReadFemPreg()
    preg_map = nsfg.MakePregMap(preg)
    for id, pregnum_value in resp.pregnum.items():
        caseid = resp.caseid[id]
        assert(pregnum_value == len(preg_map[caseid]))
    print('Success')

if __name__ == '__main__':
    main()
