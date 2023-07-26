from question import Questions
from question_data import question_data
from quiz_brain import QuizBrain

qbank = []

#loop qdata, separate text from answer, create an object from class that'll init new quest, merge newquest into bank

for questions in question_data: #loop through question_data to pull items
    questtext = questions["text"] #pull from the items being looped (questions)
    questanswer = questions["answer"]
    newquest = Questions(questtext, questanswer) #create object for the class that will init a new question from q.data
    qbank.append(newquest)

quiz = QuizBrain(qbank)

while quiz.morequest(): #remember to call the object (quiz) in order to call the method or attribute
    quiz.nextquest()

print("You've completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.qnum}")