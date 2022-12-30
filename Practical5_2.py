from ast import FloorDiv
import math
import numpy
from operator import floordiv
def add(a):
  return(sum(a))
def squareroot(a):
  return(math.sqrt(a))
def mul(a):
  return(numpy.prod(a))
def div(a,b):
  return(tuple(map(floordiv,a,b)))
def exp(a):
  return(math.exp(a))
def tan(a):
  return(math.tan(a))
def sin(a):
  return(math.sin(a))
def cos(a):
  return(math.cos(a))
def fac(a):
  return(math.factorial(a))
def log(a):
  return(math.log(a))
def i():
  user_input = input('Enter space-separated integers: ')
  B = tuple(int(item) for item in user_input.split())
  return(B)
def I():
  A = int(input("enter number -")) 
  return(A)

print("Code being developed by 202204104610033")
print(""" 
press -  
1 - Addition 
2 - squareroot 
3-multiplication 
4 - division 
5- exponent 
6 - tan 
7 - sin 
8 - cos
9 - factorial 
10 - log 
""") 

o = input("") 
if o == "1": 
    print(add(i()))
elif o == "2":
  print(squareroot(I()))
elif o == "3": 
    print(mul(i()))  
elif o == "4":
    print(div(i(),i())) 
elif o == "5": 
    print(exp(I())) 
elif o == "6":
    print(tan(I()))
elif o == "7": 
    print(sin(I())) 
elif o == "8": 
    print(cos(I())) 
elif o == "9": 
  print(fac(I())) 
elif o == "10": 
  print(log(I()))