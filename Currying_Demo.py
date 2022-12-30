import string
import re

def currying(b,c):
    def a(x):
        return b(c(x))
    return a

def currying2(b,c,d):
    def a(x):
        return b(c(d(x)))
    return a

def countsymbols(data):
    return set(re.sub(r'[a-zA-Z ]',"",data))

def countsentencewithcomma(data):
    return len(list(filter(lambda x:"," in x,data)))

def countsentence(data):
    return len(data.split("."))

def removesymbol(data):
    return data.translate(str.maketrans ('','', string.punctuation))

def countwords(data):
    return len(data.split())

def viewuniquearticles(data):
    newdata=data.split()
    return set(filter(lambda x:'a'==x or 'an'==x or 'the'==x,newdata))

def countcharacters(data):
    return len(data.replace(" ",''))

def readfile(filename):
    file1=open(filename,'r')
    return file1.read().upper()

print('Code being developed by 202204104610033')


filename='fp.txt'
getsymbols=currying(countsymbols,readfile)
getsentencenum=currying(countsentence,readfile)
getsentencewithcommanum=currying(countsentencewithcomma,readfile)
getwordsnum=currying(countwords,readfile)
getcharactersnum=currying2(countcharacters,removesymbol,readfile)
getuniquearticles=currying2(viewuniquearticles,removesymbol,readfile)

print("Unique list of number or special symbols:",getsymbols(filename))
print("No. of sentences:", getsentencenum(filename))
print("No. of sentences which are connected with comma:", getsentencewithcommanum(filename))
print("No. of words:",getwordsnum(filename))
print("Unique list of articles used:",getuniquearticles(filename))
print("No. of characters:",getcharactersnum(filename))