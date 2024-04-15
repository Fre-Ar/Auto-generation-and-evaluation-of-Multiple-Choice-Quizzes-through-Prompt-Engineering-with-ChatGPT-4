# -*- coding: utf-8 -*-

# Class representing a type of question
class QuestionType:
    def __init__(self, nOccurences, topic, topicDesc, goal, learningObjective,
                 difficulty, targetAudience, nOptions, nCorrect, allocatedTime):
        self.nOccurences = nOccurences
        self.topic = topic
        self.topicDesc = topicDesc
        self.goal = goal
        self.learningObjective = learningObjective
        self.difficulty = difficulty
        self.targetAudience = targetAudience
        self.nOptions = nOptions
        self.nCorrect = nCorrect
        self.allocatedTime = allocatedTime
        
    def __repr__(self):
        return f"""Question Type(Occurences: {self.nOccurences}, Topic: {self.topic},
                Difficulty: {self.difficulty}, Options: {self.nOptions},
                Correct: {self.nCorrect})"""

    def equals(self, question):
        # Check if all attributes are equal
        return (
            self.topic == question.topic and
            self.topicDesc == question.topicDesc and
            self.goal == question.goal and
            self.learningObjective == question.learningObjective and
            self.difficulty == question.difficulty and
            self.targetAudience == question.targetAudience and
            self.nOptions == question.nOptions and
            self.nCorrect == question.nCorrect and
            self.allocatedTime == question.allocatedTime
        )