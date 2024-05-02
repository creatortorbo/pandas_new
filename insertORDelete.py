# How to Delete and Insert Data in Pandas for Beginner
# Insert (using insert funtion here )
import pandas as pd 
print()
var = pd.DataFrame({"A":[1,2,3,4,5],"B":[6,7,8,9,10]})
print(var)
print()   # 1 is indexing 
var.insert(1,"python",var["A"])   # here 1 is indexing of A
print(var)
print()
var.insert(2,"python_1",[11,22,33,44,55])
print(var)
print()