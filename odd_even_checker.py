while True:
    start= input("do you want to play ? (yes = y , no = n)").upper()
    
    if start == "N":
        print("quiting the game")
        break

    if start == "Y":
        choise = "q"
        while choise.isdigit() == False :
            choise = input('enter your no ')
        
        choise = int(choise)

        if choise % 2 == 0:
            print("given no is even")

        else:
            print("give no is odd")



