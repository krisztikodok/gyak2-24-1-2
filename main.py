#to-do manager
tasks=[]

while True:
  print("1. Add task\n2. Remove task\n3. Task list\n4. Exit")
  choice=input("Enter the number to choose:")
  match choice:
    case "1":
      task=input(("Enter the task:"))
      tasks.append(task)
      print("Task added successfully!")
      lenght=len(tasks)
      print(f"***There are currently {lenght} pcs of tasks!***")
    case "2":
      deleting=int(input("Enter which task to delete:"))
      #list tasks
      k=1
      for i in tasks:
        print(f"{k}. "+i)

      k=1
      for i in tasks:
        if deleting==k:
          tasks.pop(k-1)
          print("Task deleted successfully!")      
        k+=1          
    case "3":
      k=1
      for i in tasks:
        print(f"{k}.: "+i)
        k+=1
      print("\n\n")
    case "4":
      break
    case _:
      print("False number")