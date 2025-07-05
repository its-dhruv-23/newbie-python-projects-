def task():
    print("----welcome to todo list program----")
    task = []
    no = int(input("enter no of task you have to do: "))

    for i in range(1,no+1):
        value = input(f"enter task {i} = ")
        task.append(value)

    print(f"your task for today \n{task}")

    while True:
        print("1 = add new task")
        print("2 = update existing task")
        print("3 = to delete a task")
        print("4 = to view the task")
        print("5 = exit the program")
        operation = int(input("enter operation you want to perform: "))

        match operation:
            case 1:
                newtask =input("enter task you want to add: ")
                task.append(newtask)
                print(f"{newtask} has been added to your list")

            case 2:
                l = task
                update = input("enter task you want to update: ")
                if update in task:
                    up = input("enter new task")
                    ind = task.index(update)
                    task[ind] = up
                    print(f"you todo list has been update form {l} to {task}")

                else:
                    print("give task in not in list. try option 1 to add a task")

            case 3:
                delete = input("enter task you want to delete: ")
                if delete in task:
                    ind = task.index(delete)
                    task.pop(ind)
                    print(f"{delete} has been deleted from your to do list")

                else:
                    print("current list does not contain given task")

            case 4:
                print(f"your task for today are \n{task}")

            case 5:
                print("exiting the todo list programm......")
                break

task()
