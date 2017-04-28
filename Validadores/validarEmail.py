'''
Created on 27 abr. 2017

@author: jgarciai
'''
import re

def compruebaErrores(email):
    patron = re.compile ("(.*)[/]")
    if (patron.match(email)):
        return "Un email no puede contener caracteres "

def compruebaEmail (email):
    patron = re.compile("[A-Za-z0-9.-_]+@[A-Za-z0-9]+.[A-Za-z-.0-9]+")
    if (patron.match(email)):
        return "es email"
    else:
        return compruebaErrores(email)
    
    
    
print (compruebaEmail("jaime@email.com"))