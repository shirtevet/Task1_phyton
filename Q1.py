# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 15:35:06 2023

@author: shirt
"""
def my_func(x1,x2,x3):

    if type(x1) != float or  type(x2) != float or type(x3) != float:
        print("Error:parameters should be float")
        return None

    else:
        denominator = x1 + x2 + x3
        Numerator = ((x1+x2+x3)*(x1+x2)*x3)
        if denominator == 0:
            a =  "Not a number - denominator equals zero"
       
        else:
            a =  Numerator/denominator
    return a
print(my_func("S",0,0))