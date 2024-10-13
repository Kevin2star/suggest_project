def add(x, y):
    print(x+y)
def subtract(x, y):
    print(x-y)
def multiply(x, y):
    print(x*y)
def divide(x, y):
    if y==0:
        print("Can't divide by zero!")
    else:
        print(x/y)
def quotient(x, y):
    if y==0:
        print("Can't divide by zero!")
    else:
        print(x//y)
def power(x, y):
    print(x**y)
def remainder(x, y):
    if y==0:
        print("Can't divide by zero!")
    else:
        print(x%y)
print("Welcome to the smallcalc.")
while(1):
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. quotient")
    print("6. power")
    print("7. remainder")
    print("8. off")
    s=int(input("Select menu : "))
    if s<=0 or s>8:
        print("Sorry, that menu doesn't exist. Try again.")
        continue
    elif s==8:
        print("If you like coding, use Python more, and Github will also help you. Power off.")
        break
    else:
        a=int(input("Choose your first integer: "))
        b=int(input("Choose your second integer: "))
        print("The result is...")
        if s==1:
            add(a, b)
        elif s==2:
            subtract(a, b)
        elif s==3:
            multiply(a, b)
        elif s==4:
            divide(a, b)
        elif s==5:
            quotient(a, b)
        elif s==6:
            power(a, b)
        else:
            remainder(a, b)
