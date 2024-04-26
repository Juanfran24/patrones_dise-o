from views import Task_View
from models import Task

class EngineerController:

    def __init__(self):

        #referencia al modelo:
        self.engineers = []

        #referencia a la vista 
        # self.view = Task_View()

    def add_engineer(self, engineer):
        self.engineers.append(engineer)

    def get_a_engineer(self, engineer_id):
        for engineer in self.engineers:
            if engineer.id == engineer_id:
                return engineer
        return "Engineer not found"
    
    def get_engineers(self):
        return self.engineers

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

    

        
