import numpy as np
from pandas.api.types import is_numeric_dtype

def mean(mean_list):
    if is_numeric_dtype(mean_list):
        mean_list = list(map(float, mean_list))
        return np.mean(mean_list, dtype=np.float64)
    else:
        answer = "This column is not numerical"
        return answer


def variance(var_list):
    if is_numeric_dtype(var_list):
        var_list = list(map(float, var_list))
        return np.var(var_list, dtype=np.float64)
    else:
        answer = "This column is not numerical"
        return answer
