# Read Python CSV files - with PANDAS
import pandas as pd
print()
csv1 = pd.read_csv("C:\\Users\\ASUS\\OneDrive\\Desktop\\pandas\\Test_new2.csv")
print(csv1)
print()

csv1 = pd.read_csv("C:\\Users\\ASUS\\OneDrive\\Desktop\\pandas\\Test_new2.csv",nrows=1) 
print(csv1)             # nrows=1 -----> With help of this we can accessing the elemnts 
print()


csv1 = pd.read_csv("C:\\Users\\ASUS\\OneDrive\\Desktop\\pandas\\Test_new2.csv",nrows=2) 
print(csv1)             # nrows=1 -----> With help of this we can accessing the elemnts 
print()                 #  nrows=2 ---> it accsseing 2 rows
print(type (csv1))      #  nrows=3  ---> it accsseing 3 rows  (and itc....)
print()
print("___________")