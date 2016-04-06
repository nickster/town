#!/usr/bin/python

import pdb

class BigMamma(object):
    
    def __init__(self):
        self.parentinit = "parent init"
        
    def parent_print(self):
        print(self.parentinit)

class BigBaby(BigMamma):
    
    def __init__(self):
        self.babyinit = "baby init"
        
    def baby_init(self):
        print (self.babyinit)
        
pdb.set_trace()