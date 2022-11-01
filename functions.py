import numpy as np

def matrix_format(images_set,flaten: bool = False):
    if bool:
        function = lambda x: np.asarray(x.convert('L')).flatten()
        return list(map(function,images_set))
    return list(map(lambda x: np.asarray(x.convert('L')),images_set))


