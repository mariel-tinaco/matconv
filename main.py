"""
Run example

>>> python main.py --xlsx "assets/Tiongco_PS1 - Annotation.xlsx" --fname "blinkerStruct.mat" -l

"""

import openpyxl
import h5py as h5 
import hdf5storage
import mat4py
from pathlib import Path

from src.functions import *

LABELS = ['Blinker']

def main (xlsx_source, mat_filename, label):
    xlsx_source = Path (xlsx_source)

    dataframe = openpyxl.load_workbook(xlsx_source)
    dataframe1 = dataframe.active

    parsed = parse_sheet(dataframe1, LABELS if label else None)

    matrix = {mat_filename.split('.')[0] : parsed}

    hdf5storage.write(matrix, '.', mat_filename, matlab_compatible=True)
    # mat4py.savemat(mat_filename, matrix)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-x', '--xlsx', type=str, required=True)
    parser.add_argument('-f', '--fname', type=str, required=True)
    parser.add_argument('-l', default=False, action='store_true')
    args = parser.parse_args()

    main (xlsx_source=args.xlsx, mat_filename=args.fname, label=args.l)

