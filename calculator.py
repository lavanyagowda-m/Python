def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "error!"
    return x/y
while True:
    print("\n simple calculator")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.Divide")
      
    choice=input("enter choice(1-5):")
    
    if choice =='5':
        print ("exit calculator")
        break
    num1=float(input("enter first number"))
    num2=float(input("enter second number")) 
    if choice=='1':
        print("result:",add(num1,num2))
    elif choice=='2':
        print("result:",subtract(num1,num2))
    elif choice=='3':
        print("result:",multiply(num1,num2))
    elif choice=='4':
        print("result:",divide(num1,num2))
    else:
        print("invalid input")
