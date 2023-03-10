from collections import defaultdict
import numpy as np


def parse_sheet (sheet, label_index) -> dict:
    class ColumnStruct:
        def __init__ (self, filename, header, label_by_index = False):
            self.filename = filename
            self.header = header
            self.bbox_and_label = []
            self.label_by_index = label_by_index

        def add (self, bbox, label):
            combine = (
                np.array([[bbox[0]]], dtype=np.uint8),
                np.array([[bbox[1]]], dtype=np.uint8),
                np.array([[bbox[2]]], dtype=np.uint8),
                np.array([[bbox[3]]], dtype=np.uint8), 
                np.array(label, dtype=np.str_ if not self.label_by_index else np.uint8)                
                )
            self.bbox_and_label.append(combine)

        def entry (self):
            return (
                np.array([self.filename], dtype=np.str_),
                np.array([self.bbox_and_label], dtype=[(elem, 'O') for elem in self.header[1:]])
            )

    container = []

    header = tuple(cell.value for cell in next(iter(sheet)))
    for row in range(1, sheet.max_row):
        col = [i[row].value for i in sheet.iter_cols(1, sheet.max_column)]
        if col[0]:
            struct = ColumnStruct(str(col[0]), header=header, label_by_index=True if label_index else False)
            struct.add (col[1:5], label_index.index(col[-1]) if label_index else col[-1])
        else:
            print("Not yet implemented")

        container.append(struct.entry())

    blinkerStruct = np.array([container], dtype=[('name', 'O'), ('bbox', 'O')])
    return blinkerStruct