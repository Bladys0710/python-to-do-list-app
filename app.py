### Updated code:
from datetime import datetime
import pandas as pd

task_lib = []


def addTask():

    def task_name():
        while True:
            task = input("Please enter a task: ")
            if task == "":
                print("Please enter a valid task.")
            # Check the first character of the task. It must be a letter!
            elif not task[0].isalpha():
                print("Please enter a valid task. Must start with a letter")
            elif len(task) > 200:
                print("Please enter a valid task. 200 characters maximum")
            else:
                # Capitalize the 1st letter.
                task = task[0].capitalize() + task[1:]
                # Enforcing punctuation at the en of the string.
                if not task[len(task)-1] in ".!?":
                    # Remove " " from the right and concatenate the input with "." using + operator.
                    task = task.rstrip(" ") + "."
                    return task
                else:
                    return task
    t_name = task_name()

    print("Set the priority. Please, chose one of the following options:")
    print(" (1) high,")
    print(" (2) medium")
    print(" (3) low")
    def priority_choice():
        while True:
            choice = input("Enter your choice: ")
            if (choice == "1"):
                return "high"
            elif (choice == "2"):
                return "medium"
            elif (choice == "3"):
                return "low"
            else:
                print("Sorry, please enter a valid option")
    t_priority = priority_choice()

    def deadline():
        while True:  # Loop until a valid date is entered
            t_date_str = input("Please enter the deadline (YYYY-MM-DD HH:MM): ")
            # Validate the input of the user. If there is an error, request another input.
            try:
                # Convert the str to date and time format.
                t_date = datetime.strptime(t_date_str, "%Y-%m-%d %H:%M")
                # Check whether the date is a future date.
                if datetime.now() < t_date:
                    # Format the time before returning
                    return t_date.strftime("%Y-%m-%d %H:%M")
                else:
                    print("Please enter a future date")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD HH:MM")
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


def deleteTask():
    listtasks()
    try:
        task_to_delete = int(input("Write the # to delete: "))
        if task_to_delete >= 0 and task_to_delete < len(task_lib):
            task_lib.pop(task_to_delete)
            print(f"The task {task_to_delete} was deleted")
        else:
            print(f"The task {task_to_delete} not found")

    except:
        print("Sorry, please enter a valid option")


if __name__ == "__main__":
    print("\n")
    print ("HELLO. THIS IS YOUR TO DO LIST!")
    while True:
        print("")
        print("What do you wanna do today?")
        print("Please select one of the following options:")
        print(" (1) Add Task")
        print(" (2) Remove Task")
        print(" (3) View Tasks")
        print(" (4) Exit")

        choice = input ("Enter your choice: ")
        print("\n")

        if (choice == "1"):
            addTask()
        elif (choice == "2"):
            deleteTask()
        elif (choice == "3"):
            listtasks ()
        elif (choice == "4"):
            break
        else:
            print("Sorry, please enter a valid option")
    print("Goodbye")
