from task import Task
from taskmanage import TaskManager
id = 1
taskmangob = TaskManager()
while True :
    print("------------------")
    print("1: Add Task ")
    print("2: Show Task list")
    print("3: Complete a task")
    print("4: Delete a task ")
    print("5: Exit")
    print("------------------")
    test = int(input("Enter Option : "))
    if test == 1 :
        idtask = id
        nametask = input("Enter Task Details : ")
        id = id + 1
        taskob = Task(idtask, nametask) 
        taskmangob.add_task(taskob)
    elif test == 2 :
        taskmangob.show_tasklist()
    elif test == 3 :
        cid = int(input("Enter Your Task Id : "))
        taskmangob.complete_a_task(cid)
    elif test == 4:
        cid = int(input("Enter Your Task Id : "))
        taskmangob.delete_a_task(cid)
    elif test == 5:
        break
    else :
        print("Invalid Input")