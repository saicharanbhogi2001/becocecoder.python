class batsman:
    teamnamme="INDIA"
    def __init__(self,name,jerseyno,role,hr):
        self.name=name
        self.jerseyno=jerseyno
        self.role=role
        self.hr=hr
        self.teamname="INDIA"
    def display(self):
        print(self.name,self.jerseyno,self.role,self.hr,self.teamname)




b=batsman("M S DHONI","7","wicketkeeper&batsman","9800")
b.display()
