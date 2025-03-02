from tkinter import *
from quiz_brain import  QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)


        self.canvas=Canvas(width=300,height=250,bg="white",highlightthickness=0)
        self.question_text=self.canvas.create_text(150,125,text=f"hello",fill=THEME_COLOR,font=("arial",20,"italic"),width=280)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        self.score_label=Label(text="score: 0 ",fg="white",bg=THEME_COLOR)
        self.score_label.grid(column=1,row=0)

        self.right_image=PhotoImage(file="images/true.png")
        self.right_button=Button(image=self.right_image,highlightthickness=0,command=self.true_pressed)
        self.right_button.grid(column=0,row=2)

        self.wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0,command=self.wrong_pressed)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()




        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.config(bg="white")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            self.canvas.itemconfig(self.question_text,text=f"you have reached the end of the quiz\n final score is {self.quiz.score}/{self.quiz.question_number} ")

    def true_pressed(self):
        is_right=self.quiz.check_answer("True")
        self.feedback(is_right)



    def wrong_pressed(self):
        is_right=self.quiz.check_answer("False")
        self.feedback(is_right)


    def feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)



















