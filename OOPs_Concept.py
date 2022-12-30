import pandas as pd
import random
import csv
from datetime import datetime
from datetime import date
from email_validator import validate_email, EmailNotValidError
import re

print('Code being developed by 202204104610033')
def isValidName(name):
    regex = "[A-Za-z ]"
    p = re.compile(regex)
 
    if(name == None):
        return False
 
    if(re.search(p, name)):
        return True
    else:
        return False

def isValidgen(gen):
    regex = "(?:m|M|f|F|t|T)$"
    p = re.compile(regex)

    if (gen == None):
        return False
    
    if(re.search(p, gen)):
        return True
    else:
        return False


def isValidPanCardNo(panCardNo):
    regex = "[A-Z]{5}[0-9]{4}[A-Z]{1}"
    p = re.compile(regex)
 
    if(panCardNo == None):
        return False
 
    if(re.search(p, panCardNo) and
       len(panCardNo) == 10):
        return True
    else:
        return False

def isValidEmail(email):
    try:
        v = validate_email(email)
        return True
    except EmailNotValidError as e:
        return False

def isValidDOB(dob):
    format = "%d-%m-%Y"
    res = True

    try:
        res = bool(datetime.strptime(str(dob), format))
    except ValueError:
        res = False

    return res

def isValidcontactno(contactNo):
    regex = "[0-9]{10}"
    p = re.compile(regex)
 
    if(contactNo == None):
        return False
 
    if(re.search(p, contactNo) and
       len(contactNo) == 10):
        return True
    else:
        return False

def isValidAddress(address):
    if(address == None):
        return False
 
    if(len(address) <= 50):
        return True
    else:
        return False

def isValidAccno(accNo):
    regex = "[0-9]{8}"
    p = re.compile(regex)
 
    if(accNo == None):
        return False
 
    if(re.search(p, accNo) and
       len(accNo) == 8):
        return True
    else:
        return False

def getAccNo():
    accno=random.randint(10000000,99999999)
    return accno

def register():
    acctype=''
    accbalance=0
    df=pd.read_csv('AccountDetails.csv')

    while(True):
        temp=int(input("Which type of account is customer wishing to open? If Savings enter 1 and if current enter 2: "))
        if temp==1:
            acctype='saving'
            break
        elif temp==2:
            acctype='current'
            break
        else:
            print('Please select a vaild option')
    
    while True:
        tempname=input("Enter Your Full Name:")
        if isValidName(tempname):
            name=tempname
            break
        else:
            print('Enter a vaild Name')

    
    while True:
        dob=input("Enter your Birth Date:" )
        if isValidDOB(dob):
            date_of_birth=dob
            break
        else:
            print('Enter Valid Date of birth')

    while True:
        gen=input("Enter Gender:")
        if isValidgen(gen):
            gender=gen
            break
        else:
            print('Enter Valid Gender')
    
    while True:
        address=input("Enter Your Address:")
        if isValidAddress(address):
            Addrss=address
            break
        else:
            print('Enter Valid Address')

    while True:
        cno=input("Enter Contact No:")
        if isValidcontactno(cno):
            contactno=cno
            break
        else:
            print('Enter Valid Contact Number')

    while True:
        tempemail=input("Enter Email:")
        if isValidEmail(tempemail):
            Email=tempemail
            break
        else:
            print('Enter Valid Email')


    while True:
        panno=input("Enter PAN number:")
        if isValidPanCardNo(panno):
            PANnumber=panno
            break
        else:
            print('Enter a valid PAN number')


    while(True):
        n=getAccNo()

        if str(n) not in df.values:
            acc_no=str(n)
            print("Account No:",acc_no)
            break

    data=[acc_no,acctype,name,date_of_birth,gender,Addrss,contactno,Email,PANnumber,accbalance]

    with open('AccountDetails.csv', 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data)

def deposit():
    df=pd.read_csv('AccountDetails.csv')
    df['Account No']=df['Account No'].astype('str')
    
    while(True):
        while True:
            accno=input('Enter Account Number: ')
            if isValidAccno(accno):
                useraccno=accno
                break
            else:
                print('Enter a valid Account number')

        useracctype=input('Enter Account Type: ').lower()
        val = df.loc[(df['Account No']==useraccno) & (df['Account Type']==useracctype),['Account Balance']]

        if(len(val)==1):
            accountbalance=int(val['Account Balance'][0])
        
            print('Minimum 1000 needs to be deposited')
            while(True):
                amt=int(input('Enter amount to be deposited: '))

                if amt>=1000:
                    accountbalance=amt+accountbalance
                    print('Available Balance:',accountbalance)
                    df.loc[(df['Account No']==useraccno) & (df['Account Type']==useracctype),['Account Balance']]=accountbalance
                    df.to_csv('AccountDetails.csv')
                    print(df['Account Balance'])
                    currenttime=datetime.datetime.now()
                    data=[useraccno,amt,currenttime,'Deposited']

                    with open('TransactionDetails.csv', 'a') as csvfile:
                        csvwriter = csv.writer(csvfile)
                        csvwriter.writerow(data)
                        break
                else:
                    print('Minimum 1000 rupees needs to be deposited.')
            break
        else:
            print('Sorry invalid account number or account type please try again')
        
        
def withdraw():
    df=pd.read_csv('AccountDetails.csv')
    df['Account No']=df['Account No'].astype('str')
    while(True):
        useraccno=input('Enter Account Number: ')
        useracctype=input('Enter Account Type: ')
        val = df.loc[(df['Account No']==useraccno) & (df['Account Type']==useracctype),['Account Balance']]
        if(len(val)==1):
            accountbalance=int(val['Account Balance'][0])
            print("Accoiunt balance:",accountbalance)
            print("Maximum 20,000 can be withdrawed on a day.")

            currentdate=date.today()
        
            newdf=pd.read_csv('TransactionDetails.csv')
            # newdf['﻿Account No']=newdf['﻿Account No'].astype('str')
            newdf['Account No']=newdf['Account No'].astype('str')

            while(True):
                # transaction = newdf.loc[(newdf['﻿Account No']==useraccno) & (newdf['Transaction']=='withdraw') & (pd.to_datetime(newdf['Transaction Date Time']).dt.date==currentdate),['Amount']]
                transaction = newdf.loc[(newdf['Account No']==useraccno) & (newdf['Transaction']=='withdraw') & (pd.to_datetime(newdf['Transaction Date Time']).dt.date==currentdate),['Amount']]
                if(len(transaction)==1):
                    todaytransaction=transaction['Amount'].sum()
                else:
                    todaytransaction=0
                
                print('You have done a withdrawal of',todaytransaction,'so you can withdraw maximum',20000-todaytransaction)
            
                while(True):                
                    amt=int(input("Enter withdrawal amount: "))
                    if amt>accountbalance:
                        print('Insufficient Balance')
                    else:
                        temp=int(accountbalance-amt)
                        print('Available balance',temp)
                        break
                
                todaybalance=abs(int(20000-todaytransaction))
                
                if amt>20000:
                    print('Withdrawal Amount should be less than 20,000 please try again')
            
                if temp<2000:
                    print("After withdrawal minimum balance of 2000 should be maintained please try again")
            
                if amt<=20000 and temp>=2000:
                    if amt<todaybalance:
                        df.loc[(df['Account No']==useraccno) & (df['Account Type']==useracctype),['Account Balance']]=temp
                        df.to_csv('AccountDetails.csv')
                    
                        currenttime=datetime.datetime.now()

                        data=[useraccno,amt,currenttime,'withdraw']

                        with open('TransactionDetails.csv', 'a') as csvfile:
                            csvwriter = csv.writer(csvfile)
                            csvwriter.writerow(data)
                            break
                    else:
                        print('You have already done a transaction so you can\'t more than',20000-todaytransaction)
            break
        else:
            print('Sorry invalid account number or account type please try again')



user=input("To register press (A) To deposit money press (B) To withdraw money press(C): ").upper()

if user=="A":
    register()

if user=="B":
    deposit()

if user=='C':
    withdraw()