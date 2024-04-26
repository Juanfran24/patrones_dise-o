from views import Task_View
from models import Task

class TaskController:

    def __init__(self):

        #referencia al modelo:
        self.tasks = []

        #referencia a la vista 
        # self.view = Task_View()

    def add_task(self, task):
        self.tasks.append(task)

    def get_a_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return "Task not found"
    
    def get_tasks(self):
        return self.tasks

    # def toggle_task_fin(self, taskIndex):
    #     pass

    # def showAllTasks(self):
    #     #llamar método en la vista:
    #     pass

    # def runController(self):
    #     #mostrar todas las tareas en la vista:
    #     self.view.showAllTasks(self.tasks)

    #     #capturar entrada de la vista

    #     #actualizar el modelo

    

        
