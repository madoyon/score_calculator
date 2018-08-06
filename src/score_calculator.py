'''
Project : Score calculator 

Calculate a score according to the ponderation etablished

Author : Marc-Antoine Doyon
Date : 05-08-2018
'''
class Score ():
    def __init__(self, numerator=0, denominator=0):
        self.numerator = numerator
        self.denominator = denominator
    
    def pourcentage(self):
        return round((self.numerator/self.denominator)*100, 2)
    
    def __str__(self):
        return f"Your score is {self.numerator} on {self.denominator} which gives {self.pourcentage()} %"
       
        
student_score = Score(2,3)
print(student_score.pourcentage())

