#creating to do list
import os
FILENAME="tasks.txt"
def load_tasks():
    tasks=[]
    if os.path.exists(FILENAME):
        with open(FILENAME,"r") as file:
            tasks=[line.strip() for line in file.readlines() if line.strip()]
    return tasks
def save_tasks(todo_list):
    with open(FILENAME,"w") as file:
        for task in todo_list:
            file.write("task\n")
def view_tasks(todo_list):
    if len(todo_list)==0:
        print("Your to-do list is empty!")
    else:
        for i,task in enumerate(todo_list,start=1):
            print(i,task)
def add_task(todo_list):
    new_task=input("Enter your new task: ").strip()
    if new_task:
        todo_list.append(new_task)
        save_tasks(todo_list)
        print("Your new task has been added!")
    else:
        print("Task cannot be empty.")
def delete_task(todo_list):
    if len(todo_list)==0:
        print("Your to-do list is empty.")
        return
    view_tasks(todo_list)
    try:
        del_one=int(input("Enter the task number to delete: "))
        index_to_del=del_one-1
        if 0<= index_to_del <len(todo_list):
            del_task=todo_list.pop(index_to_del)
            save_tasks(todo_list)
            print("Your task has been deleted: ",del_task)
        else:
            print("Invalid task number!Number is out of range.")
    except ValueError:
        print("Invalid input!Please enter a valid number.")
def main():
    todo_list=load_tasks()
    while True:
        print("     TO-DO LIST MENU     ")
        print("1.View tasks")
        print("2.Add tasks")
        print("3.Delete tasks")
        print("4.Exit")
        choice=input("Enter your choice(1-4): ")
        if choice=="1":
            view_tasks(todo_list)
        elif choice=='2':
            add_task(todo_list)
        elif choice=='3':
            delete_task(todo_list)
        elif choice=='4':
            print("See youlater!!")
            break
        else:
            print("Invalid option selected.Please choose between 1 and 4.")
main()


                                    
                    