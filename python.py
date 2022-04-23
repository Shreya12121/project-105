import math
x = [60,61,65,63,98,99,90,95,91,96]
mean = sum(x)/len(x)
print("mean of data is ", mean)
var_list = []
for i in x:
    var = (i-mean)**2
    var_list.append(var)
print("the variance of the list is", var_list)

sd = math.sqrt(sum(var_list)/len(var_list))
print("the sd of data is", sd)                  