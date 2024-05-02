import pandas as pd 
x = [1,2,3,4,5,6]

var = pd.Series(x,index= ['a','b','c','d','e','g'],dtype = "float",name="pythons")
print(var)
print()
print(type (var))
print()
print(var[2])
print()
