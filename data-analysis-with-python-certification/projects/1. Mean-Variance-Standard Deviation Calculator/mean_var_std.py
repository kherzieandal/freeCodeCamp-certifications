import numpy as np

def calculate(list1):
    if len(list1) < 9:
        raise ValueError("List must contain nine numbers.")
    # created matrix:
    matrix = np.array([list1[:3],list1[3:6],list1[6:]], dtype=float)

    # dictionary to be returned later
    calculations = {'mean': None, 'variance': None, 'standard deviation': None, 'max': None, 'min': None, 'sum': None}

    # mean index:
    calculations['mean'] = [[array.mean() for array in matrix.T], [array.mean() for array in matrix],
    matrix.mean()]

    # variance index:
    calculations['variance'] = [[array.var() for array in matrix.T], [array.var() for array in matrix], matrix.var()]

    # standard deviation index:
    calculations['standard deviation'] =[[array.std() for array in matrix.T],[array.std() for array in matrix],matrix.std()]

    # max index:
    calculations['max'] = [[array.max() for array in matrix.T], [array.max() for array in matrix], matrix.max()]

    # min index:
    calculations['min'] = [[array.min() for array in matrix.T], [array.min() for array in matrix], matrix.min()]

    # sum index:
    calculations['sum'] = [[array.sum() for array in matrix.T], [array.sum() for array in matrix], matrix.sum()]

    return calculations