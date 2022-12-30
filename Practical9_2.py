def checknum(numlist):
    l=numlist
    op=any(map(lambda x:x%2!=0,l))
    return op

obj=checknum([2,2,2,2,2])
print(obj)


# import re
# s="Hello12"

# res =all(map(lambda x:x.isdigit(),s))
# print(res)
# res = all(re.findall("\d",s))
# print(res)
# res=re.match("[0-9]*",s)
# print(res.group())