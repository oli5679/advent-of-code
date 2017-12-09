# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 22:44:51 2017

@author: oliver.cairns
"""
def process_bangs(string):
    ans = ""
    for i in range(len(string)):
        if string[i] != "!" and string[i-1] != "!":
            ans += string[i]
    if string[len(string)-1] == "!":
        ans = string[0] + ans
    return ans

print(process_bangs("<{!>}>"))
print(process_bangs("<{!>}>!"))
