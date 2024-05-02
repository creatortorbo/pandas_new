# sub for dataframe 

# here we subtration two colunms (diff oreations + , - , *,/)

import pandas as pd 
var = pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})
print()
print(var)
print()
var["c"] = var["A"] + var["B"]  
print(var) 
print()
# var                    # here we just printed dataframe
# print(var)
# print()
# here we add the two colunms in the given dic ()
var["d"] = var["A"] - var["B"]   
print(var)

print()
var["e"] = var["A"] * var["B"]   
print(var)
print()
var["f"] = var["A"] / var["B"]   
print(var)
print()