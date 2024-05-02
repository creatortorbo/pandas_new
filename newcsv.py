 #write CSV   # In pandas we are working CSV file 
import pandas as pd
dis = {"a":[1,2,3,4,5,6],"b":[1,2,3,4,5,6],"c":[1,2,3,4,5,6],"d":[11,23,45,66,77,88]
           ,"e":[11,22,33,44,55,66],"f":[12,13,14,15,16,50],"g":["bablu","vishal","aman","deepack",44,40]}
print(dis)
print()
d = pd.DataFrame(dis) 
print(d)
print()

d.to_csv("Test_new2.csv",index=False)
# here we created new csv file name is ("Test_new1.csv")
# we are removing index from csv file