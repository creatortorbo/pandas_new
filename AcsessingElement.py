import pandas as pd 
var2 = pd.DataFrame({"A":[10,20,30,40,50],"b":[15,16,17,18,19]})
print()
print(var2)
print()
# new variable 
var2["python"] = var2["A"] <= 20
var2["new pythons"] = var2["b"] <= 20
print(var2)   # here python is the columns name 
print()
