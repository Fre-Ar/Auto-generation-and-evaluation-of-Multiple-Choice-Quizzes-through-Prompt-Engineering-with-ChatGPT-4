# -*- coding: utf-8 -*-

import ipywidgets as widgets
from IPython.display import display, clear_output
from questionType import QuestionType

# Creates the Jupyter GUI to interact with (add, remove, list) the questions
def interactWithQuizManager(quizManager):
    #creates an visual output to display the list of question
    questionListOutput = widgets.Output()

    # callback function for when the add button is clicked
    def addQuestion(button):
        with questionListOutput:
            clear_output()
            # creates a question type based on the values of the input
            question = QuestionType(int(countInput.value),topicInput.value,
                        topicDescInput.value, goalInput.value,
                        learningObjectiveInput.value, difficultyInput.value,
                        targetAudienceInput.value, int(nOptionsInput.value),
                        int(nCorrectInput.value), allocatedTimeInput.value)
            # adds that question to the quiz manager
            quizManager.addQuestion(question)
            #updates the index input
            indexInput.max=len(quizManager.questions)-1
            print("Question added successfully.")
            
            # updates the displayed list of questions
            quizManager.listQuestions()

    # callback function for when the remove button is clicked
    def removeQuestion(button):
        with questionListOutput:
            clear_output()
            try:
                # removes question type based on its index (value of the index input)
                index = int(indexInput.value)
                quizManager.removeQuestion(index)
                print(f"Removed question at index {index}.")
            except ValueError:
                print("Please enter a valid integer for the question index.")
            except IndexError:
                print("Invalid index. Please enter a correct question index.")
            quizManager.listQuestions()

    # style of the labels of the inputs
    st = {'description_width': 'initial'}
    # Inputs
    topicInput = widgets.Text(description="Topic:", style=st)
    topicDescInput = widgets.Textarea(description="Topic Description:",
                                          style=st)
    goalInput = widgets.Dropdown(description="Level of Bloom's taxonomy", 
                                  options=["Remember", "Understand", "Apply",
                                           "Analyze","Evaluate","Create"],
                                            value="Understand", style=st)
    learningObjectiveInput = widgets.Text(description="Learning Objective:",
                                          style=st)
    difficultyInput = widgets.Dropdown(description="Difficulty of the MCQ", 
                                        options=["Beginner", "Intermediate",
                                                 "Advanced"], value="Intermediate",
                                            style=st)
    targetAudienceInput = widgets.Textarea(description="Audience:", style=st)
    nOptionsInput = widgets.IntSlider(description="Number of options per question:",
                                      value=4,min=2,max=6, style=st)
    nCorrectInput = widgets.IntSlider(description="Number of correct options per question:",
                                      value=1,min=1,max=6, style=st)
    allocatedTimeInput = widgets.Text(description="Allocated time:", style=st)

    # Add button inputs
    countInput = widgets.IntSlider(min=1, max=20, value=1,
                                   description="Number of Questions to add:",
                                   style=st)
    addButton = widgets.Button(description="Add Question")
    addButton.on_click(addQuestion)

    # Remove button inputs
    indexInput = widgets.IntSlider(min=0, max=min(0,len(quizManager.questions)),
                                   value=0, description="Remove Index:", style=st)
    removeButton = widgets.Button(description="Remove Question")
    removeButton.on_click(removeQuestion)

    # layout of the GUI
    L = widgets.Layout(width='33%')
    inputColumn = widgets.VBox([topicInput, topicDescInput, goalInput, learningObjectiveInput,
                           difficultyInput, targetAudienceInput, nOptionsInput,
                           nCorrectInput, allocatedTimeInput], layout=L)  
    actionColumn = widgets.VBox([countInput, addButton, indexInput, removeButton], layout=L)  
    displayColumn = widgets.VBox([questionListOutput], layout=L)
    layout = widgets.HBox([inputColumn, actionColumn, displayColumn])

    # display GUI
    display(layout)
