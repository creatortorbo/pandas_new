# What are Arithmetic Operators in Python Pandas


# here we adding two colunms and diff operators 

import pandas as pd 
var = pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})
print()
# var                    # here we just printed dataframe
print(var)
print()
# here we add the two colunms in the given dic 
var["c"] = var["A"] + var["B"]   
print(var)
print()