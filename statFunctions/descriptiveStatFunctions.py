import numpy as np
from pandas.api.types import is_numeric_dtype
from scipy import stats as st
import classes

def mean(column):
    """
    input: A string containing the column of interest
    Uses: The global dataset variable
    Output: The mean of the list
    """
    mean_list = classes.selectedDataset.getColumn(column)
    if is_numeric_dtype(mean_list):
        mean_list = list(map(float, mean_list))
        return np.mean(mean_list, dtype=np.float64)
    else:
        answer = "This column is not numerical"
        return answer

def median(column):
    
    median_list = classes.selectedDataset.getColumn(column)
    if is_numeric_dtype(median_list):
        mean_list = list(map(float, median_list))
        return np.median(mean_list)
    else:
        answer = "This column is not numerical"
        return answer

def mode(column):
    mode_list = classes.selectedDataset.getColumn(column)
    if is_numeric_dtype(mode_list):
        mode_list = list(map(float, mode_list))
        return st.mode(mode_list)
    else:
        answer = "This column is not numerical"
        return answer

def variance(column):
    """
    input: A string containing the column of interest
    Uses: The global dataset variable
    Output: The variance of the list
    """
    var_list = classes.selectedDataset.getColumn(column)
    if is_numeric_dtype(var_list):
        var_list = list(map(float, var_list))
        return np.var(var_list, dtype=np.float64)
    else:
        answer = "This column is not numerical"
        return answer

def standardDeviation(column):
    sd_list = classes.selectedDataset.getColumn(column)
    if is_numeric_dtype(sd_list):
        var_list = list(map(float, sd_list))
        return np.std(var_list, dtype=np.float64)
    else:
        answer = "This column is not numerical"
        return answer

def statCount(column):
    return len(classes.selectedDataset.getColumn(column))

def statMin(column):
    min_list = classes.selectedDataset.getColumn(column)
    if is_numeric_dtype(min_list):
        min_list = list(map(float, min_list))
        return np.min(min_list)
    else:
        answer = "This column is not numerical"
        return answer

def statMax(column):
    max_list = classes.selectedDataset.getColumn(column)
    if is_numeric_dtype(max_list):
        max_list = list(map(float, max_list))
        return np.max(max_list)
    else:
        answer = "This column is not numerical"
        return answer