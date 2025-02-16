tasks = []

def addT():
    task= input ("Please enter a task: ")
    tasks.append(task)
    print(f"The task {task} added to the list.")

def listtasks():
    if not tasks:
        print ("There are no tasks in here.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"Task # {index}, {task}")

def deleteTask ():
    listtasks()
    try:
        task_to_delete= int(input("Write the # to delete: "))
        if task_to_delete >=0 and task_to_delete < len(tasks):
            tasks.pop(task_to_delete)
            print(f"The task {task_to_delete} was deleted")
        else:
            print(f"The task {task_to_delete} not found")

    except:
        print("Sorry, please enter a valid option")

if __name__ == "__main__":
    print ("Hello this is your to do list")
    while True:
        print("")
        print("Please select one of the following option")
        print("Hello, what do you wanna do today?")
        print("(1) Add Task")
        print("(2) Remove Task")
        print("(3) View Tasks")
        print("(4) Exit")

        choise = input ("Enter your choise: ")

        if (choise =="1"):
            addT()
        elif (choise == "2"):
            deleteTask()
        elif (choise == "3"):
            listtasks ()
        elif (choise == "4"):
            break
        else:
            print("Sorry, please enter a valid option")
    print("Goodbye")

