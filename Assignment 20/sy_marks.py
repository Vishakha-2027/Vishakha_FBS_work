class SYMarks:
    def __init__(self,computer,maths,electronics):
        self.computer = computer
        self.maths = maths
        self.electronics =electronics

    def get_total(self):
        return self.computer +self.maths +self.electronics