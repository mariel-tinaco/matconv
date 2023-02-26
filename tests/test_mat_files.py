"""
Run:
>>> cd matconv
>>> python -m tests.test_mat_files
"""

import h5py as h5 

if __name__ == "__main__":
    data = 'blinkerStruct.mat'
    f = h5.File(data, 'r')
    print(f)