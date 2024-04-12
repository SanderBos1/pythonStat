import classes
import scipy.stats as sc
from pandas.api.types import is_numeric_dtype

def ttest( column1, column2, indVariance):
    """
    input: A string containing the column of interest
    Uses: The global dataset variable
    Output: The mean of the list
    """
    if is_numeric_dtype(classes.selectedDataset.getColumn(column1)) and  is_numeric_dtype(classes.selectedDataset.getColumn(column2)):
        return sc.ttest_ind(classes.selectedDataset.getColumn(column1), classes.selectedDataset.getColumn(column2), equal_var = indVariance)
    else:
        return "Please pick two numerical columns"
    

def normalTest(column):
    selectedColumn = classes.selectedDataset.getColumn(column)
    if is_numeric_dtype(selectedColumn):
        return sc.normaltest(selectedColumn)
    else:
        return "Please pick a numerical column"
