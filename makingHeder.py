
# here we Making haderfile with any rows or colunms 

import pandas as pd
print("______________________________")
print()

csv1 = pd.read_csv("C:\\Users\\ASUS\\OneDrive\\Desktop\\pandas\\Test_new2.csv") 
print(csv1)           
print()   
print("______________________________")  
print()


csv1 = pd.read_csv("C:\\Users\\ASUS\\OneDrive\\Desktop\\pandas\\Test_new2.csv",header=2)

print(csv1)           
print()   
print("______________________________")  
print()






# here another time , another rows is 3
csv1 = pd.read_csv("C:\\Users\\ASUS\\OneDrive\\Desktop\\pandas\\Test_new2.csv",header=3)

print(csv1)           
print()   
print("______________________________")  
print()

# here we changing the heading in the csv file
# we have given a new columns to the csv files

csv1 = pd.read_csv("C:\\Users\\ASUS\\OneDrive\\Desktop\\pandas\\Test_new2.csv",names=["col1","col2","col3","col4","col5","col6","col7"])

print(csv1)           
print()   
print("______________________________")  
print()


# here we making null in csv file (in hader)
csv1 = pd.read_csv("C:\\Users\\ASUS\\OneDrive\\Desktop\\pandas\\Test_new2.csv",header = None,prefix = "col")

print(csv1)           
print()   
print("______________________________")  
print()