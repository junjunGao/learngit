#!user/bin/python
#-*- encoding:utf-8 -*-

filename = raw_input('Please enter the filename: ')
with open(filename,'r') as fobj:
    for eachline in fobj:
        print(eachline.strip()) #remove '\n' at the end
