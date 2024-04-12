from pandas.api.types import is_numeric_dtype


class userDataset:
    """
    Defines the global dataset that is used by the user
    
    """
    def __init__(self, dataset):
        self.dataset = dataset

    def getColumn(self, column):
        return self.dataset[column]
    
    def getColumns(self):
        numerical_columns = []
        for column in self.dataset.columns:
            if is_numeric_dtype(self.dataset[column]):
                numerical_columns.append(column)
        return numerical_columns
    
    def getDataset(self):
        return self.dataset


# defines the global variable that holds the loaded dataset  
selectedDataset = None
