sen=input("Enter Sentence:")
l=['yellow','blue','orange','white','black','red','OC']
for color in l:
    if color in sen:
        break
match color:
    case color if color=='yellow':
        print("Monday")
    case color if color=='blue':
        print("Tuesday")
    case color if color=='orange':
        print("Wednesday")
    case color if color=='white':
        print("Thursday")
    case color if color=='black':
        print("Friday")
    case color if color=='red':
        print("Saturday")
    case color if color=='OC':
        print("Sunday")

    