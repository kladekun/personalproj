import random 
import string
class Robot:
    str1 = None
    allnames = []
    def __init__(self):
        self.name=self.random_string(2,3)
        self.allnames.append(self.name)
    def random_string(self, letter_count, digit_count):
       str1 = ''.join((random.choice(string.ascii_uppercase) for x in range(letter_count)))
       str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))

       return str1
    def reset(self):
        self.name = self.random_string(2,3)

robot=Robot()
robot2=Robot()
print(robot.name)
print(robot2.name)
print(robot2.allnames)
print(robot.allnames)
