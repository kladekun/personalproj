def is_armstrong_number(number):
    new_list = [int(d) for d in str(number)]
    power_numbers = [i ** len(new_list) for i in new_list]
    Sum = sum(power_numbers)
    if Sum == number:
        return True
    else: 
        return False
    

