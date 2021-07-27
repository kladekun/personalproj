from string import ascii_uppercase, digits
from random import choices

class Robot:
    names = set()

    def __init__(self):
        self.reset()

    def reset(self):
        letters = choices(ascii_uppercase, k=2)
        numbers = choices(digits, k=3)
        new_name = "".join(letters + numbers)
        if new_name in Robot.names:
            self.reset()
        else:
            Robot.names.add(new_name)
            self.name = new_name
        

