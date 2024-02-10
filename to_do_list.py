tasks = []

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        tasks.append(input("Enter task: "))
        print("Task added successfully!")
    elif choice == '2':
        print("\nTasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please choose a valid option.")