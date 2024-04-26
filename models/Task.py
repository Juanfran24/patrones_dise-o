import random


class Task:
    def __init__(self, kind, state, employee_id):
        self.kind = kind
        self.state = state
        self.employee_id = employee_id
        self.id = random.randint(1000, 9999)

    def set_kind(self, kind):
        self.kind = kind
    
    def get_kind(self):
        return self.kind
    
    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state
    
    def set_employee_id(self, employee_id):
        self.employee_id = employee_id

    def get_employee_id(self):
        return self.employee_id
    