class student:
    def __init__(self ,rollno,name,branch,per,bc):
        self.rollno=rollno
        self.name=name
        self.branch=branch
        self.per=per
        self.bc=bc
    def display(self):
            print(self.rollno,self.name,self.branch,self.per,self.bc)

std1=student("4A5","charan","ECE","73.5%","0")
std1.display()
std2=student("490","kamal","ECE","65%","1")
std2.display()
