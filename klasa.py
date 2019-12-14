#!/usr/bin/env python3
import sys
class Klasa:
    def __init__(self,x):
        self.x=x
    def string(self,s):
        return self.x.join(s)

class Inna:
    def __str__(self):
        return 'Siema'
i = Inna();
print(i)
