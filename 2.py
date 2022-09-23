print("1.Addition","2.Subtraction","3.Multiplication","4.Division",sep="\n")
a=int(input("Enter Your Choice:"))
b=int(input("Enter 1st Number:"))
c=int(input("Enter 2nd Number:"))
match a:
    case 1:
        print(c+b)
    case 2:
        print(b-c)
    case 3:
        print(c*b)
    case 4:
        print(b/c)
