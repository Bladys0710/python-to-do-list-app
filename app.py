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
                    # Format the time before returning
                    return t_date.strftime("%Y-%m-%d %H:%M")
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
    if not task_lib:
        print ("There are no tasks in here.")
    else:
        print("Current tasks:")
        for index, task in enumerate(task_lib):
            print(f"Task # {index}, {task}")

    def priority_order():
        prio_order = {"High": 1, "Medium": 2, "Low": 3}
        sorted_order = sorted(task_lib, key=lambda  x: prio_order[x["priority"]])
        return sorted_order


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

def suggestionTask():
    df = pd.DataFrame(task_lib)
    df.sort_values(by="deadline",ascending= True, inplace=True)
    print(f"Hello! Here are some tasks you might want to work on:")
    print(df[0:3])


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
        print("(4) Suggestion Task")
        print("(5) Exit")

        choise = input ("Enter your choise: ")
        print("\n")

        if (choise == "1"):
            addTask()
        elif (choise == "2"):
            deleteTask()
        elif (choise == "3"):
            listtasks ()
        elif (choise == "4"):
            suggestionTask()
        elif (choise == "5"):
            break
        else:
            print("Sorry, please enter a valid option")
    print("Goodbye")
