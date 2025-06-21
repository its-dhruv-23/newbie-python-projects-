import random

#loop
while True:

    #ask if user wants to play or not
    start = input(print("do you want to play the game (y = yes , n = no)")).upper()
     
        #if yes:
            #generate no:
            #check if the no is equal,high or low and print statment 
    if start == "Y":
        no = random.randint(1,100)
        ans = 1000
        
        while ans != no:
            ans = (input("enter no between 1-100: "))
            if ans.isdigit() == False :
                print("give no is not valid integer")
            if ans.isdigit() == True:
                ans = int(ans)
                if ans in range(1,101):
                    if ans < no:
                        print("too low")
                    elif ans > no :
                        print ("too high")
                    else:
                        print("you guessed correct and won the game")

                else:
                    print("enter your no in range of 1 to 100")
    elif start == "N":
        print("you choose to not play the game")    

    else:
        print("enter a valid choice")       

        #if no:
            #print:thank you 
            #break