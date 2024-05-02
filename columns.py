# here we can accessing elements in dic 
import pandas as pd
d = {"a":[1,2,3,4,5],"S":[1,2,3,4,5],"g":[2,3,4,5,6], 1 :[5,6,7,9,8]} # dic
print(d)                          
print()                             
# var = pd.DataFrame(d,columns=["a",1,"S"],index = ["a","b","c","d","g"])  # here we accessing the elements in dic with         
var = pd.DataFrame(d)
print(var)                              # we have changed index number 
print()                                                                  # colunms in dic 
print(type (var))
print()
print(var["a"][2])  # accessing elenment in dic with in colunms 
print()
