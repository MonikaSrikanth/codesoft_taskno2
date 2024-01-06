#function for addition
def addition(x,y):
    a = x+y
    print(x,"+",y,"=",a)
#function for subtraction
def subtraction(x,y):
    a = x-y
    print(x,"-",y,"=",a)
#function for multiplication
def multiplication(x,y):
    a = x*y
    print(x,"*",y,"=",a)
#function for division
def division(x,y):
    a = x/y
    print(x,"/",y,"=",a)
#menu for the user
print("|-------------------------------------------|")
print("|                                           |")
print("|              CALCULATOR                   |")
print("|   Select operation you want to perform.   |")
print("|              1.Addition                   |")
print("|              2.Subtraction                |")
print("|              3.Multiplication             |")
print("|              4.Division                   |")
print("|                                           |")
print("|-------------------------------------------|")

while True:
    ch=input("Enter choice number: ")
    if ch in('1','2','3','4'):
        try:
            print("Please enter two numbers")
            number1= float(input("Enter number: "))
            number2= float(input("Enter number: "))
        except ValueError:
            print("Invalid input.Please enter correct input(number).")
            continue
        if ch=='1':
            addition(number1,number2)       #call addition function
        elif ch=='2':
            subtraction(number1,number2)    #call subtraction function
        elif ch=='3':
            multiplication(number1,number2) #call multiplication function
        elif ch=='4':
            division(number1,number2)       #call division function

        cal_again=input("Want to do another calculation? (yes/no): ")  #check if user wants to continue
        if cal_again=='no':
            break
    else:
        print("Invalid choice")
    
