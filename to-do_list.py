print("\t\t\t\t\t****** TO-DO LIST APP ******")
print('1.Enter 1 to add task\n2.Enter 2 to view tasks\n3.Enter 3 to exit')

# Initialize an empty list for tasks
lists_task = []

def taskfunc():
    while True:
        print('\n1.Enter 1 to view tasks\n2.Enter 2 to exit\n3.Enter 3 to add more tasks\n4.Choose a task number to mark as done')
        user_instruction = input("What do you want to do: ")

        if user_instruction == '1':
            if lists_task:
                print("\t\t\t\t\t****** TASK LIST ******")
                for i, task in enumerate(lists_task, start=1):
                    print(f"{i}. {task}")
            else:
                print("No tasks added yet.")
        elif user_instruction == '2':
            print("Exiting the app.")
            exit()
        elif user_instruction == '3':
            new_task = input("Enter your task: ")
            lists_task.append(new_task)
            print("\t\t\t\t\t****** TASK ADDED ******")
        elif user_instruction == '4':
            if lists_task:
                task_number = int(input("Enter the task number you want to mark as done: "))
                if 1 <= task_number <= len(lists_task):
                    lists_task.pop(task_number - 1)
                    print("\t\t\t\t\t****** TASK MARKED AS DONE ******")
                else:
                    print("Invalid task number.")
        elif user_instruction.lower() == 'q':
            print("Exiting the app.")
            exit()
        else:
            print("Invalid input. Please try again.")

# Main loop
while True:
    print("\nEnter a task or 'q' to quit:")
    ask_task = input("Enter your task: ")
    
    if ask_task.lower() == 'q':
        print("Exiting the app.")
        break
    
    lists_task.append(ask_task)
    taskfunc()
