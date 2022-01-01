def get_outliers(dataset):

    outliers = []
    
    for c in dataset.columns:
        s=dataset[c]
        Q1 = s.quantile(0.25)
        Q3 = s.quantile(0.75)
        IQR = Q3 - Q1
        outliers+=[s[s.apply(lambda x:x < Q1 - 1.5*IQR or x > Q3 + 1.5*IQR)]]

    return outliers
