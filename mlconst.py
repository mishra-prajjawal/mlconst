class mlconst:
    """Mlconst - V1.0 """
    def __init__(self):
        self.data= []
    def mid(self,data):
        """mid() - function to find the middlemost value of a list"""
        self.data = data
        dataset = self.data
        if isinstance(dataset,list) ==True:
            self.data = data
            self.data.sort()
            #print("data",self.data) checked
            #for even number of elements
            dataset = self.data  
            if (len(dataset))%2==0:
                ndex1 = int((len(dataset)/2))
                ndex2 = int((len(dataset)/2)-1)
                return (dataset[ndex1]+dataset[ndex2])/2
            #for odd number of elements
            else:
                ndex = int((len(dataset)/2))
                return dataset[ndex]
        else:
            return "Invalid data type -> Err _datatype_ data is not a list"
    def mean(self,data):
        """mean() - function to find the mean of a list"""
        self.data = data
        dataset = self.data
        if isinstance(dataset,list)== True:
            self.data = data
            #print("data",self.data) checked 
            #print(sum(self.data)/len(self.data))checked
            return sum(dataset)/len(dataset)
        else:
            return "Invalid data type -> Err _datatype_ data is not a list"
    def mode(self,data):
        """mode() - function to find the mode of a list"""
        self.data = data
        dataset = self.data
        if isinstance(dataset,list)== True:
            self.data = data
            #print("data",self.data) checked 
            #print(sum(self.data)/len(self.data))checked
            #by default the first element is the mode because it is the most frequent
            return max(set(dataset), key=dataset.count) 
        else:
            return "Invalid data type -> Err _datatype_ data is not a list"
    def stade(self,data):
        """stade() - function to find the standard deviation of a list"""
        self.data = data
        dataset = self.data
        if isinstance(dataset,list)== True:
            self.data = data
            #print("data",self.data) checked 
            #print(sum(self.data)/len(self.data))checked
            #by default the first element is the mode because it is the most frequent
            mean = sum(dataset)/len(dataset)
            #print(mean) checked
            #print(sum([(i-mean)**2 for i in dataset])/len(dataset)) checked
            return (sum([(i-mean)**2 for i in dataset])/len(dataset))**0.5
        else:
            return "Invalid data type -> Err _datatype_ data is not a list"
    def varce(self,data):
        """variance() - function to find the variance of a list"""
        self.data = data
        dataset = self.data
        if isinstance(dataset,list)== True:
            self.data = data
            #print("data",self.data) checked 
            #print(sum(self.data)/len(self.data))checked
            #by default the first element is the mode because it is the most frequent
            mean = sum(dataset)/len(dataset)
            #print(mean) checked
            #print(sum([(i-mean)**2 for i in dataset])/len(dataset)) checked
            return sum([(i-mean)**2 for i in dataset])/len(dataset)
        else:
            return "Invalid data type -> Err _datatype_ data is not a list"
    def percentiles(self,data,percentile=0):
        """percentiles() - function to find the percentiles of a list"""
        self.data = data
        self.data.sort()
        dataset = self.data
        if isinstance(dataset,list)== True:
            #print("data",self.data) #checked
            #print("data",self.data) checked
            #print("percentile",percentile) checked
            #print("percentile/100",percentile/100) checked
            #print("len(dataset)",len(dataset)) checked
            #print("len(dataset)*percentile/100",len(dataset)*percentile/100) checked
            #print("int(len(dataset)*percentile/100)",int(len(dataset)*percentile/100)) checked
            if percentile == 0:
                return "Invalid percentile -> Err _per_ no value passed after data ",self.data
            else:
                return dataset[int(len(dataset)*percentile/100)]
        else:
            return "Invalid data type -> Err _datatype_ data is not a list"
    def mkdatasets(self,start,end,total_assets):
        self.start = start
        self.end = end
        self.assets= total_assets
        r_assets=[] #assets to be returned
        for i in range(self.assets):
            import random 
            r_assets.append(random.uniform(start,end))
        return r_assets
    def mkdatasets_normal(self,start,end,total_assets):
        #make a normal distribution of data
        self.start = start
        self.end = end
        self.assets= total_assets
        r_assets=[] #assets to be returned
        for i in range(self.assets):
            import random 
            r_assets.append(random.normalvariate(start,end))
        return r_assets



