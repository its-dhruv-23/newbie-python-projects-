print("basic calculato")
while True:
    start = input("do you wish to calculate ? (y = yes, n = no)").upper()

    if start == "N":
        print("Quiting from cal... ")
        break

    if start == "Y":
        a = int(input("enter value of a "))
        b = int(input("enter value of b "))
        result = None
        choice = "w"
        print("1 = add\n2=subtrack\n3=multipyle\n4=divide\n5=power\n6=modulo")
        while choice not in [1,2,3,4,5,6]:
                    choice = int(input("enter valid choice"))

        match choice:
            case 1:
                result = a+b
            case 2:
                result = a-b
            case 3:
                result = a*b
            case 4 :
                result = a/b
            case 5:
                result = a**b
            case 6:
                result = a%b
        print (result)
