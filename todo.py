import sys
sys.path.append("todo_app")


def change():
    tasks = readfile()
    choice = int(input("Delete or Change Element \n 1 : Delete \n 2 : Change \n 3 : Append \n"))

    if choice == 1:
        
        view(tasks)
        choice = input("Insert the entry that you want to delete : \n")
        if choice in tasks:
            tasks.remove(choice)
        else:
            print("The entry you want to delete does not exist in the todo list.")
    elif choice == 2:
        
        view(tasks)
        choice = input("Insert the entry that you want to replace : \n")
        if choice in tasks:
            index = tasks.index(choice)
            new_entry = input("Replace with : ")
            tasks[index] = new_entry
        else:
            print("The entry you want to replace does not exist in the todo list.")
    elif choice == 3:
        
        view(tasks)
        choice = input("Insert the entry that you want to append with [end to stop]: \n")
        
        while choice != "end":
        
            tasks.append(choice)
            view(tasks)
            choice = input("Insert the entry that you want to append with [end to stop]: \n")

    with open("data.txt", "w") as file:  
        for task in tasks:
            file.write(task + "\n")




def reset():
  f = open("data.txt","w")
  print("data has been cleared")
  f.close()


def readfile():
    tasks = []
    with open("data.txt") as file:
        for line in file:
            line = line.strip()  
            tasks.append(line)
        return tasks


def view(tasks):
    print("-------")
    for i in range(len(tasks)):
        print(tasks[i])
    print("-------")
def menu():
    

    choice = int(input("Welcome \n 1 : View todo list \n 2 : Change todo list \n 3 : Reset todo list \n 4 : Exit \n"))
    while (1):
        tasks = readfile()

        if choice == 1 :
            view(tasks)
        if choice == 2:
            change()
        if choice == 3:
            reset()
        if choice == 4 :
            print("Goodbye!")
            sys.exit()
        
        choice = int(input("\n 1 : View todo list \n 2 : Change todo list \n 3 : Reset todo list \n 4 : Exit \n"))

menu()
