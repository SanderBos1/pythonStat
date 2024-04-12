import classes
import scipy.stats as sc

def ttest( column1, column2, indVariance):
    """
    input: A string containing the column of interest
    Uses: The global dataset variable
    Output: The mean of the list
    """
    answer = sc.ttest_ind(classes.selectedDataset.getColumn(column1), classes.selectedDataset.getColumn(column2), equal_var = indVariance)
    testStatistic = answer.statistic
    pvalue = answer.pvalue

    return {
        "pValue": str(pvalue),
        "testStatistic": str(testStatistic)
    }
    

def normalTest(column):
    selectedColumn = classes.selectedDataset.getColumn(column)
    answer = sc.normaltest(selectedColumn)
    pvalue = answer.pvalue
    return {
        "pValue": str(pvalue),
    }
