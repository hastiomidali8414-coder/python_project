from asyncio import tasks
from os import remove


def show_tasks():
    if len(tasks) == 0:
        print("There are no tasks")
    else:
        print("\nTasks list:")
        for i, task in enumerate(tasks, 1)
            print(f"{i}. {task}")

while True:
    print("\n--- TODO APP ---")
    print("1. Add task")
    print("2. show tasks")
    print("3. delete task")
    print("4. Exit")

    choice = intput ("Choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added")

    elif choice == "2":
        show_tasks()

  elif choice == "3":
      show_tasks()
      num = int(input("Enter task number: "))
      if 0 < num <= len(tasks):
          remove = tasks.pop(num - 1)
          print(f"{Removed} deleted")

  elif choice == "4":
    print("Goodbye!")
    break

  else:
      print("Invalid choice")
