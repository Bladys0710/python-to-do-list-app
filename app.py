from datetime import datetime
import pandas as pd

task_lib = []


def addTask():

    t_name = input ("Please enter a task: ")

    print("Set the priority. Please, chose one of the following options")
    print("(1) high,")
    print("(2) medium")
    print("(3) low")
    def priority_choice():
        while True:
            choise = input("Enter your choice: ")
            if (choise == "1"):
                return "high"
            elif (choise == "2"):
                return "medium"
            elif (choise == "3"):
                return "low"
            else:
                print("Sorry, please enter a valid option")
    t_priority = priority_choice()

    def deadline():
        while True:  # Loop until a valid date is entered
            t_date_str = input("Please enter the deadline (YYYY-MM-DD): ")
            # Validate the input of the user. If there is an error, request another input.
            try:
                # Convert the str to date and time format.
                t_date = datetime.strptime(t_date_str, "%Y-%m-%d")
                # Check whether the date is a future date.
                if datetime.now() < t_date:
                    return t_date
                else:
                    print("Please enter a future date")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
    t_deadline = deadline()

    task_lib.append({"task": t_name, "priority": t_priority, "deadline": t_deadline})
    print("\n")
    print(f"The task '{t_name}' with priority '{t_priority}' and deadline '{t_deadline}' was added to the list.")
    print("\n")

    # print(pd.DataFrame(task_lib))


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
        if task_to_delete >= 0 and task_to_delete < len(tasks):
            tasks.pop(task_to_delete)
            print(f"The task {task_to_delete} was deleted")
        else:
            print(f"The task {task_to_delete} not found")

    except:
        print("Sorry, please enter a valid option")


if __name__ == "__main__":
    print("\n")
    print ("HELLO THIS IS YOUR TO DO LIST")
    print("\n")
    while True:
        print("")
        print("Hello, what do you wanna do today?")
        print("Please select one of the following option")
        print("(1) Add Task")
        print("(2) Remove Task")
        print("(3) View Tasks")
        print("(4) Exit")

        choise = input ("Enter your choise: ")
        print("\n")

        if (choise == "1"):
            addTask()
        elif (choise == "2"):
            deleteTask()
        elif (choise == "3"):
            listtasks ()
        elif (choise == "4"):
            break
        else:
            print("Sorry, please enter a valid option")
    print("Goodbye")

