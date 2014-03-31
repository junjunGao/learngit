#!user/bin/env python
#-*- encoding:utf-8 -*-

import re

keyword = ("auto","break","case","char","const","continue","default",  
  
"do","double","else","enum","extern","float","for",  
  
"goto","if",'int',"long","register","return","short",  
  
"signed","static","sizeof","struct","switch","typedef","union",  
  
"unsigned","void","volatile","while","printf")
precomment = ''
result = ''
word = ''

with open('test.c','r') as files:
    for line in files:
        if line != '\n':
            precomment = "%s%s" %(precomment,line.lstrip()) #It is a more efficient method?
        else:
            precomment = "%s%s" %(precomment,line)
        #line = line.replace('\n',' ')
        #line = line.replace('\t','')
        #precomment += line;

comment = re.sub( '\/\*(\s|.)*?\*\/|\/\/.*?\s',' ',precomment )
comment = comment.replace('\n',' ')
prestring = comment.replace('\t','')


print(prestring)

for element in prestring:
    if element.isalpha():       # isalpha
        word += element 
    else:
        if element.isspace():
            if word != '':                 #judge if the string is a keyword
                if word[0].isalpha() or word[0].isdigit():
                    for s in keyword:
                        if cmp(s,word)==0:
                            result += word + ' '
                            word = ''
                            break
                    if word != '':
                        word = 'V'
                        result += word
                        word = ''
                else:
                    result += word
                    word = ''
        else:
            if element.isdigit():
                word += element
            else:
                if word == '':
                    result += element
                else:
                    for s in keyword:
                        if cmp(s,word) == 0:
                            result += word + element
                            word = ''
                            break
                    if word != '':
                        if not word[0].isalpha() and word[0] != '_':
                            result += word + element
                            word = ''
                        else:
                            word = 'V' + element
                            result += word
                            word = ''
                    #else:
                     #   print(word+'9')
                      #  result += word + element
                       # word = ''
print(result)
