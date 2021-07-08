class Students:
    student_class="student"

    def __init__(self,name, age, student_class):
        self.name=name
        self.age=age
        self.student_class=student_class

    def average_score(self,n1,n2,n3):
        score = (n1+n2+n3) /3
        return score


John=Students("John","20","Art Class")
averagescore=John.average_score(50,60,78)
print("Average score: ",averagescore)