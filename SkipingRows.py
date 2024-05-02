import pandas as pd
csv1 = pd.read_csv("C:\\Users\\ASUS\\OneDrive\\Desktop\\pandas\\Test_new2.csv",usecols=["g","c","e","d"])
print(csv1)
print("__________________")
print()
# here we Skiping the elments with slacing 
csv1 = pd.read_csv("C:\\Users\\ASUS\\OneDrive\\Desktop\\pandas\\Test_new2.csv",skiprows=[0])
print(csv1)
print("___________________")
print()
