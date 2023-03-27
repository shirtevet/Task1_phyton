# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 16:02:23 2023

@author: shirt
"""

def revword(b:str):
            return b.lower()[::-1]
    

def countword():
     num_line = 0
     a = open('text.txt',"r")
     counter = 0
     for line in a:
           l = line.split(' ')
           num_line += 1
           if num_line == 1:
               word = l[0].lower().strip()
               counter +=1 
               print(word)
               
           else:
               for i in l:
                      w = revword(i).strip()
                      if w == word:
                          counter +=1
                          
     print(counter)
countword()               
                  

           