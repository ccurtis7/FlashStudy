from graphics import *
from button import Button

class QAManager:
    def __init__(self, win):
        # Define the input fields for the question and answer
        self.question_input = Entry(Point(250, 300), 15).draw(win)
        self.question_input_label = Text(Point(145, 300), "Question:").draw(win)
        
        self.answer_input = Entry(Point(250, 250), 15).draw(win)
        self.answer_input_label = Text(Point(145, 250), "Answer:").draw(win)
        
        self.save_button = Button(win, Point(150, 150), 45, 32, "Save")
        self.save_button.activate()

        self.quit_button = Button(win, Point(350, 150), 45, 32, "Quit")
        self.quit_button.activate()

        self.clicked = win.getMouse()

    def save_question_answer(self):
        question, answer = self.question_input.getText(), self.answer_input.getText()
        
        # Save the question and answer to a file
        with open("questions.txt", "a") as f: f.write(f"{question}\n{answer}\n")
        
        # Clear the input fields
        self.question_input.setText(""), self.answer_input.setText("")

    # def event_handlers(self):
    #     pt = self.clicked
    #     while


win = GraphWin("Question and Answer Manager", 500, 500)
win.setCoords(0, 0, 500, 500)
# Initialize the QAManager object
qa_manager = QAManager(win)
