def change(b,c,d):
    def a(x):
        return b(c(d(x)))
    return a

def kilometertometer(measurement):
    return measurement*1000

def metertofoot(measurement):
    return measurement*3.28084

def foottoinch(measurement):
    return measurement*12

if __name__ == '__main__':
    print('Code is being developed by 202204104610033')
    transform = change(foottoinch,metertofoot,kilometertometer)
    val=float(input('Enter the value you want to convert: '))
    e=transform(val)
    print("Value of converstion from kilometer to inch is",e)