


print("""Simple Calculator
Operation Number:
1 = addition
2 = subtraction
3 = multiplication
4 = division""")

x = int(input("Enter your operation number:"))
if x <=4:
    a = int(input("Enter Value 1:"))
    b = int(input("Enter Value 2:"))
else:
    print("Enter correct operation number!!1 to 4")

def addition(a,b):
    return (a+b)
def subtraction(a,b):
    return (a-b)
def multiplication(a,b):
    return (a*b)
def division(a,b):
    return (a/b)

if x==1:
    print("Output =",addition(a,b))
elif x==2:
    print("Output =",subtraction(a,b))
elif x==3:
    print("Output =",multiplication(a,b))
elif x==4:
    print("Output =",division(a,b))









