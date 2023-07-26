# TODO ask question
# TODO check answer
# TODO check if quiz finish

class QuizBrain:

    def __init__(self, qlist): #initializer to set up starting points for the object
        self.qnum = 0 #will have a default value at 0 to start at and ascend the number of questions
        self.qlist = qlist #will pass over into the init input
        self.score = 0

    def nextquest(self): #method to get next question
        currentquest = self.qlist[self.qnum] #retrieve the item at the current question number from the question list
        #currentquest is like an object while in a method; to call text, currentquest.text
        self.qnum += 1 #start at and increase the next question by 1
        useranswer = input(f"Q.{self.qnum}: {currentquest.text} (True/False)?: ") #made a variable in order to checkanswer()
        self.checkanswer(useranswer, currentquest.answer)
        #call method here and assign parameters that'll be positional and correspondent to checkanswer method below

    def morequest(self): #method to return a boolean and determine if loop should stop or return another question
        return self.qnum < len(self.qlist)
        #return True (keep looping) if the current qnum is less than total qnum & vice versa

    def checkanswer(self, useranswer, correctanswer): #method to check the answer and track score
        if useranswer.lower() == correctanswer.lower():
            print("Correct")

            self.score += 1
        else:
            print("Wrong")
        print(f"The correct answer is: {correctanswer}")
        print(f"Your final score is {self.score}/{self.qnum}")
        print("\n")





