# adding to series 
import pandas as pd
s1 = pd.Series(12,index = [1,2,3,4,5,6,7])
s2 = pd.Series(12,index = [1,2,3,4])
r = s1+s2
print(r)
print()
print(type(r))
print()
               # just adding two 