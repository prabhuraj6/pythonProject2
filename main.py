def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("select: ")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
while True:
    choice = input("Enter choice(1/2/3/4):")
    if choice in ('1','2','3','4'):
        num1 = int(input("Enter first num: "))
        num2 = int(input("Enter second num: "))
        if choice=='1':
            print(num1,"+",num2,"=",add(num1,num2))
            if choice == '2':
                print(num1, "-", num2, "=", sub(num1, num2))
                if choice == '3':
                    print(num1, "*", num2, "=", mul(num1, num2))
                    if choice == '1':
                        print(num1, "/", num2, "=", div(num1, num2))
                        next_calculation=input("yes or no")
                        if next_calculation=="no":
                            break

