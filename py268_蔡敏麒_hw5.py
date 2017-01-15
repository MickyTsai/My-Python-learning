class student():
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.grades = []
        
    def add(self,grades):
        self.grades.append(grades)
        
    def avg(self):
        return sum(self.grades)/len(self.grades)
    
    def fcount(self):
        count = 0
        for g in self.grades :
            if g < 60 :
                count += 1
        return count
    
    
    
            
        
    
        

s1 = student("Tom","M")
s2 = student("Jane","F")
s3 = student("John","M")
s4 = student("Ann","F")
s5 = student("Peter","M")
s1.add(80)
s1.add(90)
s1.add(55)
s1.add(77)
s1.add(40)
s2.add(58)
s2.add(87)
s3.add(100)
s3.add(80)
s4.add(40)
s4.add(55)
s5.add(60)
s5.add(60)

        
