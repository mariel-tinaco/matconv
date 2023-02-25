"""
Run example

>>> python -m utils.mat_io

"""
from scipy.io import loadmat, savemat
from pprint import pprint
import numpy as np


def load (filename):

    mat_contents = loadmat(filename)
    pprint(mat_contents)


if __name__ == "__main__":

    digitStruct = np.array(
        [
            [
                (np.array(['1.png'], dtype='<U5'), 
                    np.array(
                        [
                            [
                                (np.array([[30]], dtype=np.uint8), np.array([[43]], dtype=np.uint8), np.array([[7]], dtype=np.uint8), np.array([[19]], dtype=np.uint8), np.array([[5]], dtype=np.uint8))
                            ]
                        ], 
                        dtype=[('height', 'O'), ('left', 'O'), ('top', 'O'), ('width', 'O'), ('label', 'O')]
                        )
                    ),     
                (np.array(['2.png'], dtype='<U5'), 
                    np.array(
                        [
                            [
                                (np.array([[23]], dtype=np.uint8), np.array([[99]], dtype=np.uint8), np.array([[5]], dtype=np.uint8), np.array([[14]], dtype=np.uint8), np.array([[2]], dtype=np.uint8)),        
                                (np.array([[23]], dtype=np.uint8), np.array([[114]], dtype=np.uint8), np.array([[8]], dtype=np.uint8), np.array([[8]], dtype=np.uint8), np.array([[1]], dtype=np.uint8)),
                                (np.array([[23]], dtype=np.uint8), np.array([[121]], dtype=np.uint8), np.array([[6]], dtype=np.uint8), np.array([[12]], dtype=np.uint8), np.array([[10]], dtype=np.uint8))
                            ]
                        ], 
                        dtype=[('height', 'O'), ('left', 'O'), ('top', 'O'), ('width', 'O'), ('label', 'O')]
                    )
                ),       
                (np.array(['3.png'], dtype='<U5'), 
                    np.array(
                        [
                            [
                                (np.array([[16]], dtype=np.uint8), np.array([[61]], dtype=np.uint8), np.array([[6]], dtype=np.uint8), np.array([[11]], dtype=np.uint8), np.array([[6]], dtype=np.uint8))
                            ]
                        ],      
                        dtype=[('height', 'O'), ('left', 'O'), ('top', 'O'), ('width', 'O'), ('label', 'O')]
                    )
                )
            ]
        ],   
        dtype=[('name', 'O'), ('bbox', 'O')]
    )

    # print(digitStruct)

    load ('blinkerStruct.mat')
