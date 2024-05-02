# write CSV   # In pandas we are working CSV file 
import pandas as pd
dis = {"a":[1,2,3,4,5,6],"b":[1,2,3,4,5,6],"c":[1,2,3,4,5,6]}
print(dis)
print()
d = pd.DataFrame(dis) # d ---> is dataframe
print(d)
print()
# d.to_csv("Test_new.csv")  #here we create CSV file for dataFrame 
   # and we can see this csv file where in main file in saved 
d.to_csv("Test_new1.csv",index=False)
# here we created new csv file name is ("Test_new1.csv")
# we are removing index from csv file