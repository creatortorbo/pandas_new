# here we using indexing in the csv file

# Read Python CSV files - with PANDAS
import pandas as pd
print("______________________________")
print()

csv1 = pd.read_csv("C:\\Users\\ASUS\\OneDrive\\Desktop\\pandas\\Test_new2.csv") 
print(csv1)           
print()   
print("______________________________")  
print()

# here we calling the indexing from the csv files 
csv1 = pd.read_csv("C:\\Users\\ASUS\\OneDrive\\Desktop\\pandas\\Test_new2.csv",index_col="g") 
print(csv1)           
print()   # here we cloums as index
          # using  "g"  here as index 
print("_______________________________")
