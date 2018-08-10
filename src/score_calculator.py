'''
Project : Score calculator 

Calculate a score according to the ponderation etablished

Author : Marc-Antoine Doyon
Date : 05-08-2018
'''

dict_score = {'A+':'4.3','A':'4.0','A-':'3.7','B+':'3.3','B':'3.0','B-':'2.7','C+':'2.3','C':'2.0','C-':'1.7'
,'D+':'1.3','D':'1.0','E':'0.5','F':'0.0'}
dict_letter = {range(90,101):'A+',range(85,90):'A',range(80,85):'A-',range(77,80):'B+',range(73,77):'B'
,range(70,73):'B-',range(65,70):'C+',range(60,65):'C',range(57,60):'C-',range(54,57):'D+',range(50,54):'D'
,range(35,50):'E',range(0,35):'F'}

class Score():
    def __init__(self, numerator=0, denominator=0):
        self.numerator = numerator
        self.denominator = denominator
    
    def pourcentage(self):
        return round((self.numerator/self.denominator)*100, 2)
    
    def __str__(self):
        return f"Your score is {self.numerator} on {self.denominator} which gives {self.pourcentage()} %"
       
        
class Cours():
    def __init__(self, name = "", credit = 0, test = []):
        self.name = name
        self.credit = credit
        self.test = test
    
    def global_score(self):
        total = []
        for s,p in self.test:
            total.append((p/100)*s)
        return sum(total)
    
    def letter_score(self):
        return dict_letter[self.global_score()]

class Student():
    def __init__(self, courses = []):
        self.courses = courses
    
    def calculate_GPA(self):
        nb_credits = []
        score = []
        for i in self.courses:
            score.append(i.global_score())
            nb_credits.append(i.credit)

