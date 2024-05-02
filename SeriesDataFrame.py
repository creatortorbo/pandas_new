# two Series join and create Dataframe 
import pandas as pd 
sr = {"s":pd.Series([1,2,3,4]),"r":pd.Series([1,2,3,4])}
# print(sr)
print()
var3 = pd.DataFrame(sr)

print(var3)
print()
print(type(var3))
print()