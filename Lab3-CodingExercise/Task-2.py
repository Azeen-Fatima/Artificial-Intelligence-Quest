def cel_to_fahr(c):
    return (c*9/5)+32
def fahr_to_cel(f):
    return (f-32)*5/9

a=int(input("Enter 1 if you want to convert into celsius and Enter 2 if you want to convert into fahrenheit."))
if a==1:
    x=float(input("Enter Temrature in Fahrenheit."))
    print(x,"F in celsius is ",fahr_to_cel(x),"C")
elif a==2:
    x=float(input("Enter Temrature in Celsius."))
    print(x,"C in fahrenhiet is ",cel_to_fahr(x),"F")
else:
    print("Invalid input")