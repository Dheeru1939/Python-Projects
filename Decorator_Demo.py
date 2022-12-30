import pandas as pd

def decorator(toppingsadder):
    def wrapper(a,b):
        return toppingsadder(a,b)
    return wrapper

@decorator
def topping_add(a,b):
    return a+b

toppings={
    'Extra Toppings':['Extra Cheese','Paneer','Baby corn','Pineapple','Sweet corn'],
    'Extra Cost':[100,80,50,60,30]
    }

df=pd.DataFrame(toppings)

print("Plain Pizza cost: 200")
print(df)

base_price=200

while True:
    print("Enter Bill if all the toppings you wished are added and you want the final bill.")

    val=input('What topping do wish to add please select one by one: ')

    if 'bill'==val.lower():
        price=0
        base_price=topping_add(price,base_price)
        print("Final Bill:",base_price)
        break

    elif int(val)<len(df) and int(val)>=0:
        val=int(val)
        price=df.loc[val,'Extra Cost']
        base_price=topping_add(price,base_price)
        print(df.loc[val,'Extra Toppings'],"is being added")
        print('Bill Price: ',base_price)
    
    else:
        print('Enter a valid input')
