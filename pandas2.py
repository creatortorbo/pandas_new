import pandas as pd 
dic  ={"name" :['python','c','c++','java'],"por":[12,13,14,15,16],"Rank":[1,2,3,4]} 
print()
print(dic)
print()
var1 = pd.Series(dic)   # In this we are using dictonary in instread of list
print(var1)
print()
print(type(var1))
print()


