import math
from operator import itemgetter

print('code being developed by 202204104610033')
# Q1
#i
numsqr=lambda x:x**2
print('Square of number:',numsqr(2))

#ii
num_sqrt=lambda x,y: math.sqrt((x**2)+(y**2))
print('Square root of number:',num_sqrt(2,3))

#iii
num_avg=lambda *x:sum(x)
print('Average:',num_avg(2,2,2))

#iv
uniq_letter = lambda x:set(x)
print(uniq_letter(input('Enter String: ').lower()))


# Q2

list_dict=[{'Name': 'Parimal', 'Programming': 'Julia', 'Year of Experience': 9}, {'Name': 'Mayur', 'Programming': 'C', 'Year of Experience': 4}, 
{'Name': 'Hiren', 'Programming': 'Python', 'Year of Experience': 6}]

val=lambda x:sorted(x,key=itemgetter('Programming'))
print(val(list_dict))