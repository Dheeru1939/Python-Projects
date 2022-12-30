import random
import math

def num_converter(num,base):
    temp=num
    final_val=''
    while(True):
        temp_reminder=temp%base
        temp=math.floor(temp/base)

        if temp_reminder>=10:
            final_val=chr(55+temp_reminder)+final_val
        else:
            final_val=str(temp_reminder)+final_val

        if temp<base:
            final_val=str(temp)+final_val
            break

    return final_val

def check_val(val,userval):
    if int(userval) == val:
        print("You are right!",val)
        return 1
       
    elif int(userval) < val:
        print("Ohh! Your guess is too low.\n")

    elif int(userval) > val:
        print("Ohh! Your guess is too high.\n")

j=0

val=random.randint(1,100)

for x in range(0,3):   
    userval=input("Guess the number:")
    k=check_val(val,userval)

    if k==1:
        break

    else:
        j=j+1

if j==3:
    print('\nSorry you didn\'t guess in time. The number was',val)

base=random.randint(2,16)
print('\nRandomly generated base number is',base)
num=int(input('\nEnter the number you want to convert in the given base: '))

print('\nNumber after conversion from decimal to base',base,'is',num_converter(num,base))

