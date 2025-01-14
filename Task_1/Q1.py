#Define a function named “triple_and” that takes three parameters and returns True only if they are all True and False otherwise

def triple_and(var1, var2, var3):
    if ((var1=="True" and var2=="True") and var3=="True"):
        return True
    else:
        return False

var1=input("enter var1: \n")
var2=input("enter var2: \n")
var3=input("enter var3: \n")

print(triple_and(var1,var2,var3))
