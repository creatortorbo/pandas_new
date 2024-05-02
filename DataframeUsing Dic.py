# here using data sturure 
import pandas as pd
d = {"a":[1,2,3,4,5],"S":[1,2,3,4,5]} # dic
print(d)                            # if ,6 elements in the dic is their one side than 
print()                             #it cant be run (it create error)
var = pd.DataFrame(d)             # than          # the length will be same in bouth side 
print(var)
print()
print(type (var))
print()