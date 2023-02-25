"""
Run example

>>> python main.py --xlsx "assets/Tiongco_PS1 - Annotation.xlsx"

"""

import openpyxl
from scipy.io import savemat
from pathlib import Path

from src.functions import *

def main (xlsx_source):
    xlsx_source = Path (xlsx_source)

    dataframe = openpyxl.load_workbook(xlsx_source)
    dataframe1 = dataframe.active

    matrix = {
        '__globals__' : [],
        '__header__' : b'MATLAB 5.0 MAT-file, Platform: PCWIN64, Created on: Fri Feb 24 17:11:54 2023',
        '__version__' : '1.0',
        'blinkerStruct' : parse_sheet(dataframe1) 
    }

    savemat('blinkerStruct.mat', mdict=matrix)

    
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-x', '--xlsx', type=str, required=True)
    args = parser.parse_args()

    main (xlsx_source=args.xlsx)

