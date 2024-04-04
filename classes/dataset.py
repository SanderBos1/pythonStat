class userDataset:
    """
    Defines the global dataset that is used by the user
    
    """
    def __init__(self, dataset):
        self.dataset = dataset

    def getColumn(self, column):
        return self.dataset[column]
    
    def getColumns(self):
        return self.dataset.columns
    
    def getDataset(self):
        return self.dataset


# defines the global variable that holds the loaded dataset  
selectedDataset = None
