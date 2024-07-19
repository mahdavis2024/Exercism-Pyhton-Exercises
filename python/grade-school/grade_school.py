class School:
    def __init__(self):
        self.sch = {}
        self.adds = []

    def add_student(self, name, grade):
        self.sch[grade] = self.sch.get(grade, [])
        if name not in self.roster():
            self.sch[grade].append(name)
            self.adds.append(True)
        else:
            self.adds.append(False)
   
    def roster(self):
        return [name
                for grade in sorted(self.sch.keys())
                for name in sorted(self.sch[grade])]

    def grade(self, grade_number):
        return sorted(self.sch.get(grade_number, []))

    def added(self):
        return self.adds
