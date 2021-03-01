import pandas as pd

pd.set_option("display.max_columns",50)  # options for panda displays
pd.set_option("display.max_rows",100)
pd.set_option("display.width",1000)

canadian_youtube=pd.read_csv("CAvideos.csv")
british_youtube=pd.read_csv("GBvideos.csv")
concat_data= pd.concat([canadian_youtube,british_youtube])

left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])

join_data = left.join(right, lsuffix='_CAN', rsuffix='_UK')

#print(join_data.head(5))  # show only start of data
#print(canadian_youtube.shape,british_youtube.shape, concat_data.shape, join_data.shape)
#print(concat_data.head())

# practice using the join function on 2 dataframes
file1="list1.csv"
file2="list2.csv"

list1=pd.read_csv(file1)
list2=pd.read_csv(file2)

print(list1)
print(list2)

# using the JOIN function
list3=list1.join(list2.set_index("id"), on="id")
print(list3)

#using the MERGE function
merge_data=pd.merge(list1,list2,on="id")
print(merge_data)