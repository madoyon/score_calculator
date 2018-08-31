'''
Project : Score calculator 

Calculate a score according to the ponderation etablished

Author : Marc-Antoine Doyon
Date : 05-08-2018
'''
class RangeDict(dict):
    def __getitem__(self, item):
        if type(item) != range: # or xrange in Python 2
            for key in self:
                if item in key:
                    return self[key]
        else:
            return super().__getitem__(item)


dict_score = RangeDict({'A+':'4.3','A':'4.0','A-':'3.7','B+':'3.3','B':'3.0','B-':'2.7','C+':'2.3','C':'2.0','C-':'1.7'
,'D+':'1.3','D':'1.0','E':'0.5','F':'0.0'})
dict_letter = RangeDict({range(90,101):'A+',range(85,90):'A',range(80,85):'A-',range(77,80):'B+',range(73,77):'B'
,range(70,73):'B-',range(65,70):'C+',range(60,65):'C',range(57,60):'C-',range(54,57):'D+',range(50,54):'D'
,range(35,50):'E',range(0,35):'F'})

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
            total.append((int(p)/100)*int(s))
        return sum(total)
    
    def letter_score(self):
        return dict_letter[int(self.global_score())]
    
    def ponderation_left(self):
        ponderation = []
        for s,p in self.test:
            ponderation.append(p)
        return (100-sum(ponderation))
    
    def expected_score(self):
        p_left = self.ponderation_left()
        for i in range(0,101):
            print('Expected next score : {} \tNew score updated : {} ---> {}'.format(i,round((i/100*p_left+self.global_score()),3),dict_letter[int(i/100*p_left+self.global_score())]))
        return("\nThere you go, I wish you good luck for what's comming next!!\n\n")


    def __str__(self):
        return f'\n\nCourse : {self.name} \t Credits : {self.credit}\nActual score : {self.global_score()} ---> {self.letter_score()}\nPonderation left : {self.ponderation_left()}\n'

class Student():
    def __init__(self, courses = []):
        self.courses = courses
    
    def calculate_GPA(self):
        nb_credits = []
        score = []
        for i in self.courses:
            score.append(i.global_score())
            nb_credits.append(i.credit)

while(True) :
    welcome = """
    Welcome to the score calculator!!!\n
    Using this tool, you will be able to calculate your present course and receive estimation according to your scores\n
    You will need your xams scores and ponderation of each of them\n
    Let's get started!\n
    """
    print(welcome)
    student = Student()
    entering_courses = True
    while(entering_courses):
        try: 
            name_course, credits_course = input("Enter your course name and the number of credits : \n").split()
            name_course = Cours(name_course, credits_course)
            
        except ValueError:
            print("Error : Please enter 2 arguments : name of the course and credits (exemple : Mathematic 3)\n")
            continue
        entering_tests = True
        tests = []
        while(entering_tests):
            try:
                s,p = input("Enter your exam result and the ponderation : ").split()
                exam = (int(s),int(p))
                tests.append(exam)
                
            except ValueError:
                print("Error : Please enter 2 arguments : result(%) and ponderation(%) (exemple : 80 35)\n")
                continue
            next = input("Would you like to enter another score? (Y/N) : ")
            if('n' in next.lower()):
                name_course.test = tests
                entering_tests = False
            elif('y' in next.lower()):
                continue
        student.courses.append(name_course)
        next = input('Would you like to enter another course? (Y/N) : ')
        if('n' in next.lower()):
            entering_courses = False
            for i in student.courses:
                print(i)
                print(i.expected_score())
        elif('y' in next.lower()):
                continue
        
    break