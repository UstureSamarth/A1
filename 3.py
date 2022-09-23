print("Enter Sides Of Triangle")
a,b,c=int(input()),int(input()),int(input())
print("a.For isosceles Triangle\nb.For right angle Triangle\nc.Equilateral Triangle\nd.Exit")
x=(input("Enter Your Choice:"))
match x:
    case x if x=='a':
        if(a==b!=c or b==c!=a or c==a!=b):
            print("Isoscales Triangle")
        else:
            print("not Isoscales Triangle")
    case x if x=='b':
        if(a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2):
            print("Right Angle Triangle")
        else:
            print("not Right Angle Triangle")
    case x if x=='c':
        if(a==b==c):
            print("Equilateral Triangle")
        else:
            print("not Equilateral Triangle")
    case _:
        print("Invalid Choice")





