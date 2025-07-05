#make a basic phone book
dic={}
no = "vv"
while no.isdigit()==False :
    no = input("enter how much no you want to save: ")
for i in range(0 , int(no)):
    name= input("enter the name of contact: ")
    contact = "vv"
    while contact.isdigit() == False:
        contact = input("enter no of you contact: ")
    dic[name]=int(contact)
while True:
    
    print("1 = add new no.")
    print("2 = remove existing no")
    print("3 = view you phone list")
    print("4 = change existing no")
    print("5 = quite the program")

    choice = "vv"
    while choice.isdigit() == False or int(choice) not in [1,2,3,4,5]:
        choice = input("enter operation you want to perform: ")

    match int(choice):
        case 1:
            new_c = input("enter name of you new contact: ")
            new_n = "ee"
            while new_n.isdigit() == False:
                new_n = input("enter no of new contact: ")

            dic[new_c]= new_n

        case 2:
            del_c = input("enter name of contact you want to delete: ")
            if del_c in dic:
                dic.pop(del_c)
                print(f"{del_c} has been removed from the dictonary")

            else:
                print(f"{del_c} does not exist in yout current phone book")

        case 3:
            print("your current phone book is :")
            print(dic)

        case 4:
            up_name = input("enter contact name you want to update: ")
            if up_name in dic:
                up_no="jj"
                while up_no.isdigit()==False:
                    up_no = input("enter no you want to update: ")
                dic[up_name]=up_no
                print(f"no of {up_name} id updated")
            else:
                 print(f"{up_name} does not exist in yout current phone book")

        case 5:
            print("quiting the program...")
            break
