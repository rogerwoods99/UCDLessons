# import SAS

import pandas as pd
from sas7bdat import SAS7BDAT
with SAS7BDAT('urbanpop.sas7bdat') as file:
    df_sas = file.to_data_frame()

##########################
# import Stata
#############################
import pandas as pd
data = pd.read_stata('urbanpop.dta')

##########################
# import HDF5
#############################
import h5py
filname='long word.hdf5'
data = h5py.File(filename, 'r')  # r=read
print(type(data))

# print the structure of the HDF5 file. We can think of the structure as directories
for key in data.keys()
    print(key)

# print the structure of the data in the "meta" directory
for key in data['meta'].keys():
    print(key)

# set "strain" equal to the value of the Strain field in the strain dataset
strain = data['strain']['Strain'].value

##########################
# import MATLAB
#############################

import scipy.io
filename = 'workspave.mat'
mat = scipy.io.loadmat(filename)
print(type(mat))
print(type(mat['x']))  # this variable "x" could be a numpy.ndarray
# MATLAB data is a stored as a dictionary with keys=Variable names and values=objects assigned to variables

##########################
# import from Relational Database using SQLite
#############################

from sqlalchemy import create_engine
engine = create_engine('sqlite:///Northwind.sqlite')
table_names = engine.table_names()
print(table_names)

##########################
# SQL query connection
#############################

from sqlalchemy import create_engine  # create the engine
import pandas as pd
engine = create_engine('sqlite:///Northwind.sqlite')  # connect to engine
con = engine.connect()
rs = con.execute("SELECT * FROM Orders")  # send SQL command
df = pd.DataFrame(rs.fetchall())   # save to DataFrame
df.columns = rs.keys()  # get the correct column names
con.close()
print(df.head())   # print the start of the data

# can also do the above using the WITH construct

from sqlalchemy import create_engine  # create the engine
import pandas as pd
engine = create_engine('sqlite:///Northwind.sqlite')  # connect to engine
with engine.connect() as con:
    rs = con.execute("SELECT OrderID, OrderDate, ShipName FROM Orders")
    df = pd.DataFrame(rs.fetchmany(size=5))  # only fetch 5 rows
    df.columns =rs.keys()

# add the WHERE clause to filter the selection
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee WHERE EmployeeID >= 6')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# This can all be done with one line of code
from sqlalchemy import create_engine  # create the engine
import pandas as pd
engine = create_engine('sqlite:///Northwind.sqlite')  # connect to engine
df = pd.read_sql_query("SELECT * FROM Orders", engine)

# JOIN TABLES
from sqlalchemy import create_engine  # create the engine
import pandas as pd
engine = create_engine('sqlite:///Northwind.sqlite')  # connect to engine
df = pd.read_sql_query("SELECT OrderID, CompanyName FROM Orders INNER JOIN Customers on Orders.CustomerID = Customers.CustomerID", engine)
print(df.head())
