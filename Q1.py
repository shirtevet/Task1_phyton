# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 15:35:06 2023

@author: shirt
"""
def my_func(x1,x2,x3):

    if type(x1) != float or  type(x2) != float or type(x3) != float:
        if x1 == 0 and x2 == 0 and x3==0:
           return "Not a number - denominator equals zero"
           
        if (type(x1) != int and type(x1) != float ) or ( type(x2) != int and type(x2) != float) or (type(x3) != int and type(x3) != float):
            return None
        else:
            b="Error:parameters should be float"
            return b

    else:
        denominator = x1 + x2 + x3
        Numerator = ((x1+x2+x3)*(x2+x3)*x3)
        if denominator == 0:
            a =  "Not a number - denominator equals zero"
       
        else:
            a =  Numerator/denominator
    return a

print(my_func(31.1,4.2, 2.2))
print(my_func(8.0,0.0,-8.0))
print(my_func(0, 0, 0))
print(my_func(31.1,10, 2.2))
print(my_func(31.1,list("john"), 2.2))