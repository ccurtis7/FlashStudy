from graphics import *
from button import Button

class QAManager:
    def __init__(self, win):
        self.answer_input = Entry(Point(250, 250), 15).draw(win)
        self.answer_input_label = Text(Point(145, 250), "Answer:").draw(win)
        
        self.question_input = Entry(Point(250, 300), 15).draw(win)
        self.question_input.setFill("lightgreen")
        self.question_input_label = Text(Point(145, 300), "Question:").draw(win)
        
        self.save_button = Button(win, Point(150, 150), 45, 32, "Save")
        self.answer_input.setFill("lightgreen")
        self.save_button.activate()

        self.quit_button = Button(win, Point(350, 150), 45, 32, "Quit")
        self.quit_button.activate()

    def save_inputs(self):
        question, answer = self.question_input.getText(), self.answer_input.getText()
        
        # Save the question and answer to a file
        with open("Sample.txt", "a") as f: f.write(f"Question: {question}\nAnswer: {answer}\n")
        
        # Clear the input fields
        self.question_input.setText(""), self.answer_input.setText("")

    def upload(self):
        self.pt = win.getMouse()

        while not self.quit_button.clicked(self.pt):
            if self.save_button.clicked(self.pt):
                self.save_inputs()
                self.pt = win.getMouse()

win = GraphWin("Question and Answer Manager", 500, 500)
win.setCoords(0, 0, 500, 500), win.setBackground("wheat")

qa_manager = QAManager(win)
qa_manager.upload()
