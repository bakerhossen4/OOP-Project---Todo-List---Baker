
from task import Task

class TaskManager :
    def __init__(self):
        self.tasklist = []

    def add_task( self, taskob ):
        self.tasklist.append(taskob)
        print(f"Task ID {taskob.id} Added Successfully")
    def show_tasklist (self):
        print("****** Showing Task Lists ******")
        print(f"ID ------------ Details -------------- Completed Status")
        for i in self.tasklist :
            print(f"{i.id}\t\t{i.name}\t\t{i.completed}")
        print("********************************")
    def complete_a_task( self, id ):
        print("--------------------------------------------")
        for i in self.tasklist :
            if i.id == id :
                i.completed = True
                print(" Good ! Your Task has been completed")

        print("--------------------------------------------")
        
    def delete_a_task( self, id ):
        print("--------------------------------------------")
        for i in self.tasklist :
            if i.id == id :
                if i.completed == True :
                    self.tasklist.remove(i)
                    print(" Good ! Your Task has been deleted")
                else :
                    print("Task is not completed. For deleting task you have to complete the task")
        print("--------------------------------------------")
    