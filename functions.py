import numpy as np

def matrix_format(images_set):
    return list(map(lambda x: np.asarray(x.convert('L')),images_set))