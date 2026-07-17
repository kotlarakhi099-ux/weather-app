todo_list=[]
def show_tasks():
    print("\n__tasks__")
    if not todo_list:
        print("your to do list is empty")
    else:
        for index, task in enumerate(todo_list):
            print(f"{index}.{task}")
while True:
    action=input("enter your option(add)(view)(remove)(exit):")
    if action=="add":
        item=input("enter task to list:")
        todo_list.append(item)
        print(f"{item} added successfully")
    elif(action=="view"):
        show_tasks()
    elif(action=="remove"):
        show_tasks()
        if todo_list:
            try:
                task_num=int(input("enter i to remove:"))
                if 1<=task_num<=len(todo_list):
                 removed=todo_list.pop(task_num-1)
                 print(f" '{removed} ' has been removed. ")
                else:
                   print("invalid task number.")
            except ValueError:
                print("please enter a valid no:")
    elif (action=="exit"):
        print("good bye ")
        break
    else:
        print("invalid option")


