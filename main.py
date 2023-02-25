"""
Run example

>>> python main.py --xlsx "assets/Tiongco_PS1 - Annotation.xlsx -l"

"""

import openpyxl
from scipy.io import savemat
from pathlib import Path

from src.functions import *

LABELS = ['Blinker']
MAT_FILENAME = 'blinkerStruct.mat'

def main (xlsx_source, label):
    xlsx_source = Path (xlsx_source)

    dataframe = openpyxl.load_workbook(xlsx_source)
    dataframe1 = dataframe.active

    parsed = parse_sheet(dataframe1, LABELS if label else None)

    matrix = {
        '__globals__' : [],
        '__header__' : b'MATLAB 5.0 MAT-file, Platform: PCWIN64, Created on: Fri Feb 25 11:11:11 2023',
        '__version__' : '1.0',
        'blinkerStruct' : parsed
    }

    savemat(MAT_FILENAME, mdict=matrix)

    
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-x', '--xlsx', type=str, required=True)
    parser.add_argument('-l', default=False, action='store_true')
    args = parser.parse_args()

    main (xlsx_source=args.xlsx, label=args.l)

