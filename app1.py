# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:24:47 2019

@author: PPRRIINNCCEE
"""

import json
from difflib import get_close_matches
data=json.load(open("data.json"))
def translate(w):
    v=w.lower()
    if v in data:
        output=data[v]
        for i in output :
            print(v,end="")
            print(" : ",end="")
            print(i)
    elif w.title() in data:
        output=(data[w])
        for i in output :
            print(w,end="")
            print(" : ",end="")
            print(i)
    elif w.upper() in data:
        output=(data[w])
        for i in output :
            print(w,end="")
            print(" : ",end="")
            print(i)
    elif get_close_matches(v,data.keys(),n=1,cutoff=0.8):
        sub=get_close_matches(v,data.keys(),n=1,cutoff=0.8)[0]
        print("did you mean %s : " %sub)
        ans=input("press y for yes and n for no :")
        if ans =="y"or ans=="Y":
            return translate(sub)
        else:
            print("sorry!! please try again.no such word exist")
    else:
        print("sorry!! please try again.no such word exist")
c='y'
while(c!='n'):
    user=input("enter a key to search: ")
    translate(user)
   
    c=input("press y to search again and n to stop :")
