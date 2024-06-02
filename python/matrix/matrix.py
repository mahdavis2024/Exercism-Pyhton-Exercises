class Matrix:
    def __init__(self, matrix_string):
        self.string = matrix_string
        
    def row(self, index):
        self.index = index - 1
        splited = self.string.split('\n')
        single = splited[self.index].split()
        rrr = []
        for i in range(len(single)):
            rrr.append(int(single[i]))
        return rrr

    def column(self, index):
        self.index = index - 1
        splited = self.string.split('\n')
        matr = []
        col = []
        for i in range(len(splited)):
            matr.append(splited[i].split())
        for i in range(len(splited)):
            col.append(int(matr[i][self.index]))
        return col
            
