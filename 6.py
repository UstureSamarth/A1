a=input("Enter String:")
a=a.strip()
match a:
    case a if ' ' in a:
        print("MultiWord")
    case a if ' ' not in a:
        print("SingleWord")
        