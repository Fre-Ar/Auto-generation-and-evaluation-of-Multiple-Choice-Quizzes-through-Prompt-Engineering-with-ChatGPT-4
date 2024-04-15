# -*- coding: utf-8 -*-

# Class that contains and manages the question types
class QuizMakerManager:
    def __init__(self):
        self.questions = []

    # adds a question type to the list of questions
    def addQuestion(self, question):
        for q in self.questions:
            if question.equals(q):
                q.nOccurences += question.nOccurences
                return
        self.questions.append(question)

    # removes a question type from the list of questions based on its index
    def removeQuestion(self, index):
        if index < len(self.questions):
            del self.questions[index]
        else:
            print("Invalid question index.")

    # lists all the added question types
    def listQuestions(self):
        for idx, question in enumerate(self.questions):
            print(f"{idx}: {question}")


