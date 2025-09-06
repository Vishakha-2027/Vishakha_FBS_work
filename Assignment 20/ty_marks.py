class TYMarks:
    def __init__(self,theory,practical):
        self.theory = theory
        self.practical =practical
    
    def get_total(self):
        return  self.theory + self.practical