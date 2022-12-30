def change(b,c,d):
    def a(x):
        return b(c(d(x)))
    return a

def kilometertometer(measurement):

    try:
        val=float(measurement)*1000
        return val
    
    except:
        return None,False


def metertofoot(measurement,containval=True):

    if not containval:
        return "Kilometer to meter raised an error"

    try:
        val=float(measurement)*3.28084
        return val
    except:
        return None,False


def foottoinch(measurement,containval=True):
    if not containval:
        return "meter to foot raised an error"
    try:
        val=float(measurement)*12
        return val
    except:
        return "foot to inch raised an error"

if __name__ == '__main__':
    print('Code is being developed by 202204104610033')
    transform = change(foottoinch,metertofoot,kilometertometer)
    
    val=input('Enter the value you want to convert: ')
    e=transform(val)
    print("Value of converstion from kilometer to inch is",e)