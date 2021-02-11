# use API to download a CSV files

from urllib.request import urlretrieve
import pandas as pd
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
urlretrieve(url, 'winequality-white.csv')
df = pd.read_csv('winequality-white.csv', sep=';')
print(df.head())

# Same as above but don't use the retrieve function

from urllib.request import urlretrieve
import pandas as pd
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
df = pd.read_csv(url, sep=';')
print(df.head())

##########################################################################
########################################################################
# Import non flat files from web.
# Note that the output of pd.read_excel() is a Python dictionary
# with sheet names as keys and corresponding DataFrames as corresponding values

import pandas as pd

# Assign url of file: url
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'

# Read in all sheets of Excel file: xls
xls = pd.read_excel(url, sheet_name=None)

# Print the sheetnames to the shell
print(xls.keys())

# Print the head of the first sheet (using its name, NOT its index)
print(xls['1700'].head())