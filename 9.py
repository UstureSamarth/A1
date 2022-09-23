year=int(input("Enter Year:"))
match year:
    case year if year%100==0 and year%400==0:
        print("Century Leap Year")
    case year if year%100==0:
        print("Century Non Leap Year")
    case year if year%4==0:
        print("Non Century Leap Year")
    case year:
        print("Non Century Non Leap Year")