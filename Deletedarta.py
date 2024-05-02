# here we delete the values in from dataframe
import pandas as pd
print()
var = pd.DataFrame({"A":[1,2,3,4,5],"B":[6,7,8,9,10],
                    "C":[11,12,13,14,15],"D":[16,17,18,19,20]})
print(var)
print()
var.pop("B")  # here we have delated "B" colunms in dataframe 
print(var)
print()
# here we insert "E" in this dataframe 
var.insert(3,"E",[11,22,33,44,55])
print(var)
print()

