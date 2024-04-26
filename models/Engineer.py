import random


class Engineer:
    def __init__(self, role):
        self.role = role
        self.tasks = []
        self.id = random.randint(100, 999)

    def set_role(self, role):
        self.role = role

    def get_role(self):
        return self.role

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks