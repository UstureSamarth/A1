month=int(input("Enter Month Number:"))
match month:
    case month if month in (1,3,5,7,8,10,12):
        print("31 Days")
    case month if month in (4,6,9,11):
        print("30 Days")
    case month if month==2:
        print("28 or 29 Days")
    case _:
        print("Invalid Month Number")
print("Hello World")
    

    
    

