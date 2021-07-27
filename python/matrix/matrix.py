class Matrix:
    def __init__(self, matrix_string):
        self.split_string = matrix_string.splitlines()
        self.matrix = [[int(u) for u in i.split()] for i in self.split_string]
        pass

    def row(self, index):
        real_index = index - 1
        return self.matrix[real_index]

    def column(self, index):
        real_index = index - 1
        column_list = [i[real_index] for i in self.matrix] 
        return column_list
        
