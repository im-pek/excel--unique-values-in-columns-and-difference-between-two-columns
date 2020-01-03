import pandas as pd
import numpy as np
  
df = pd.read_excel(r"L:\My Documents\Desktop\file_1.xlsx")

array1=df['Worksheet 1 Name'].unique() #shows unique values in an excel column in python list format

df2 = pd.read_excel(r"L:\My Documents\Desktop\file_2.xlsx")

array2=df2['Worksheet 2 Name'].unique() #shows unique values in an excel column in python list format

print(np.setdiff1d(array1, array2)) #excel cells in column 1 not in column 2, and vice versa