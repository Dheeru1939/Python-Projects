from csv import DictReader
from itertools import groupby
from operator import itemgetter
from string import Template

print('Code being developed by 202204104610033')
class CustomTemplate(Template):
	delimiter = '#'

with open("orderBill.csv", 'r') as f:
	
	dict_reader = DictReader(f)
	
	list_of_dict=(list(dict_reader))

for k in list_of_dict:
    del k['ï»¿ ']
 
 
l = sorted(list_of_dict,key = itemgetter('Bill No'))

temp_string='\t\t\t Dheeraj Sons\n\t Bill No: #billno \t\t\t Order No:#orderno \n\t Customer Name: #custname \n\t\t Product Name\t\t\tPrice\tQuantity'
temp_product_detail='\t #productname \t\t #Price \t #Quantity'
temp_total='\t Total Amount: \t\t\t\t #totalprice'
template = CustomTemplate(temp_string)
template1= CustomTemplate(temp_product_detail)
template2=CustomTemplate(temp_total)

total=0
for key, value in groupby(l,key = itemgetter('Bill No')):
    for k in value:
        output = template.substitute(billno=k['Bill No'], orderno=k['Order No'], custname=k['Customer Name'].upper())
        print('\n',output)
        output = template1.substitute(productname=k['Product Name'], Price=k['Price'], Quantity=k['Quantity'].upper())
        total=total+float(k['Price'])
        print(output)
        break

    for k in value:
        output = template1.substitute(productname=k['Product Name'], Price=k['Price'], Quantity=k['Quantity'].upper())
        total=total+float(k['Price'])
        print(output)

output=template2.substitute(totalprice=total)
print('\n',output)




print('\nCode being developed by 202204104610033\n')
import os
import time
import win32api
import win32con

path = 'F:\MCA\SEM-1\Functional Programming Paradigm'

dir_list=os.listdir(path)
# print(dir_list)

l1=[]

if os.path.isdir(path):

    for f in dir_list:
        split_tup = os.path.splitext(f)
        
        # extract the file name and extension
        file_name = split_tup[0]
        file_extension = split_tup[1]
        
        print("File Name: ", file_name)
        print("File Extension: ", file_extension)
        print("File Size: {}KB".format(os.path.getsize(f)))

        # if file_extension=='.pdf':
        #     os.remove(f)

    print(l1)


    print('File having size 0KB')
    for f in dir_list:
        if os.path.getsize(f)==0:
            print('File Name:',f)
            print('Last Access Time: ', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getatime(f))))
            print('File Owned by',win32api.GetUserNameEx (win32con.NameSamCompatible))

    print('List of sub directories available in the root directory')

    for it in os.scandir(path):
        if it.is_dir():
            print(it.path)
