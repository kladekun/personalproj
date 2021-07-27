import string
class PhoneNumber:
    def __init__(self, number: str):
        exclist =string.punctuation + ' ' + '+1'
        table = str.maketrans("", "", exclist)
        self.number: str = number.translate(table)
        if len(self.number) != 10 or self.number[0] == "0" or self.number[3] == '0':
            raise ValueError("Invalid Input")
        self.area_code = number[0:3]
    def pretty(self):
        #Adds the brackets to the first 3 integers
        pretty_1 =  self.number.replace(self.number[0:3], "("+self.number[0:3]+")")
        #Adds dashes to the next three integers  
        pretty_final = pretty_1.replace(pretty_1[5:8], "-"+pretty_1[5:8]+"-") 
        return pretty_final
        
