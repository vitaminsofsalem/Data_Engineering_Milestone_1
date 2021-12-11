import DataProcTools.DataCleaning.MissingValues as MissingValuesUnit
import pandas as pd
from io import StringIO

testcsv=StringIO('''
Age,Weight,Height
22,60,160
22,80,NA
14,NA,170
16,90,190
NA,78,160
NA,NA,180
NA,NA,167
''')

print(MissingValuesUnit.get_nan_values_percentage(pd.read_csv(testcsv)))
