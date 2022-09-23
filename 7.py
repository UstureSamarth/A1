num=int(input("Enter Number:"))
match num:
    case num if num>0:
        print("Positive")
    case num if num<0:
        print("Negative")
    case num:
        print("Zero")