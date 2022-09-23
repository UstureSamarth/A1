str1=input("Enter String 1:")
str2=input("Enter String 2:")
match str1:
    case str1 if str1==str2:
        print("String are Identical")
    case str1 if str1>str2:
        print(str2,"comes first then",str1)
    case str:
        print(str1,"comes first then",str2)

    