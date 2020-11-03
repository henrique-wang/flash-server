# -*- coding: utf-8 -*-
"""
@author: Henrique Igai Wang

Class that represents each product from an specific store
"""
import json

class Product:
    def __init__(self,id, name, price):
        self.id = id
        self.name = name
        self.price = str(price)

    def __str__(self):
        string = "ID: %s;  Name: %s;  Price: %s" %(self.getID(), self.getName(), self.getPrice())
        return string

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price