print("----word counter in string----")
while True:
    choice = "jfjf"
    while choice not in ["Y","N"]:
        choice = input("do you want to play the game (y = yes , n = no)").upper()

    if choice =="Y":
        st = input("enter you string: ")
        count = list(st.split())
        ans = len(count)

        print(ans)

    else:
        print("quiting the game...")
        break