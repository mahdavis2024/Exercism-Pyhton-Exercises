class Garden:
    def __init__(self, diagram, students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']):
        self.seeds = {
            'G':'Grass',
            'C':'Clover',
            'R':'Radishes',
            'V':'Violets'
        }
        self.students = sorted(students)
        self.diagram = diagram.split('\n')
    
    def plants(self,name):
        ind = 2* self.students.index(name)
        return [self.seeds[self.diagram[0][ind]], self.seeds[self.diagram[0][ind+1]], self.seeds[self.diagram[1][ind]], self.seeds[self.diagram[1][ind+1]] ]
        
        
