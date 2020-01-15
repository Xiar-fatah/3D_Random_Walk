#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 13:44:17 2020

@author: kiarr99
"""

def test(x):
    x.append(1)
    return x 
if __name__ == "__main__":
    x = [0]
    test(x)
    print(x)