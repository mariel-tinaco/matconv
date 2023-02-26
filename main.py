"""
Run example

>>> python main.py --xlsx "assets/Tiongco_PS1 - Annotation.xlsx" -l

"""

import openpyxl
import h5py as h5 
import hdf5storage
from scipy.io import savemat, loadmat
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
        MAT_FILENAME.split('.')[0] : parsed
    }

    hdf5storage.write(matrix, '.', MAT_FILENAME, matlab_compatible=True)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-x', '--xlsx', type=str, required=True)
    parser.add_argument('-l', default=False, action='store_true')
    args = parser.parse_args()

    main (xlsx_source=args.xlsx, label=args.l)

