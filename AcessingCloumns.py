# Read Python CSV files - with PANDAS
# here we accesing all the cloumns (one by one and multiple cloumns )
import pandas as pd
print()
csv1 = pd.read_csv("C:\\Users\\ASUS\\OneDrive\\Desktop\\pandas\\Test_new2.csv")
print(csv1)
print()
# Accesing cloumns 
csv1 = pd.read_csv("C:\\Users\\ASUS\\OneDrive\\Desktop\\pandas\\Test_new2.csv",usecols=["a"])

print()
csv1 = pd.read_csv("C:\\Users\\ASUS\\OneDrive\\Desktop\\pandas\\Test_new2.csv",usecols=["b"])
print(csv1)
print()

csv1 = pd.read_csv("C:\\Users\\ASUS\\OneDrive\\Desktop\\pandas\\Test_new2.csv",usecols=["c"])
print(csv1)
print()

csv1 = pd.read_csv("C:\\Users\\ASUS\\OneDrive\\Desktop\\pandas\\Test_new2.csv",usecols=["d"])
print(csv1)
print()

csv1 = pd.read_csv("C:\\Users\\ASUS\\OneDrive\\Desktop\\pandas\\Test_new2.csv",usecols=["e"])
print(csv1)
print()

csv1 = pd.read_csv("C:\\Users\\ASUS\\OneDrive\\Desktop\\pandas\\Test_new2.csv",usecols=["f"])
print(csv1)
print()

csv1 = pd.read_csv("C:\\Users\\ASUS\\OneDrive\\Desktop\\pandas\\Test_new2.csv",usecols=["g"])
print(csv1)
print()
print()

print("here we Accesed all the complited columns in csv file ")
print()
print("__________________________")
print()


# Acessing multiple cloumns 

csv1 = pd.read_csv("C:\\Users\\ASUS\\OneDrive\\Desktop\\pandas\\Test_new2.csv",usecols=["g","c","e","d"])
print(csv1)
print()                    
print("__________________________")
print()


# here also we can accessing the multiple with indexing 
csv1 = pd.read_csv("C:\\Users\\ASUS\\OneDrive\\Desktop\\pandas\\Test_new2.csv",usecols=[0,1,2])
print(csv1)
print()
print("__________________________")
print()