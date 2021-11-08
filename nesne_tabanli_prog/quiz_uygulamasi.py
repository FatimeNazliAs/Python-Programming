
class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer


    def checkAnswer(self,answer):
        return self.answer==answer

#print(q1.checkAnswer('Python'))
#print(q2.checkAnswer('c'))

class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0

    def getQuestion(self):
        return self.questions[quiz.questionIndex]

    def displayQuestion(self):
        question=self.getQuestion()
        print(f" Soru {self.questionIndex+1}: {question.text}")


        for q in question.choices:
            print('-'+q)

        answer=input('cevap: ')
        print(question.checkAnswer(answer))
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question=self.getQuestion()

        if question.checkAnswer(answer):
            self.score+=1

        self.questionIndex+=1
        self.displayQuestion()

    def loadQuestion(self):
        if len(self.questions) ==self.questionIndex:
            self.showScore()
        else:
            self.displayQuestion()

    def showScore(self):
        pass




















q1=Question('en iyi programlama dili hangisidir?',['c#','Python','Javascript','Java'],'Python')
q2=Question('en popüler programlama dili hangisidir?',['Python','Javascript','c#','Java'],'Python')
q3=Question('en çok kazandıran programlama dili hangisidir?',['Javascript','c#','Java','Python'],'Python')
questions=[q1,q2,q3]

quiz=Quiz(questions)
quiz.displayQuestion()



