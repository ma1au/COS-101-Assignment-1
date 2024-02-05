import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz_data import quiz_data


def show_question():
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal")

    feedback_label.config(text="")
    next_btn.config(state="disabled")


def check_answer(choice):
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    if selected_choice == question["answer"]:
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        feedback_label.config(text="Incorrect!", foreground="red")

    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

# Function to Restart the Quiz
def restart_quiz():
    global current_question, score
    # Reset current_question and score
    current_question = 0
    score = 0
    # Update the score label
    score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))

    # Enable all choice buttons
    for button in choice_btns:
        button.config(state="normal")

    # Display the first question
    show_question()

# Function to move on to the next question or end the quiz if the questions have finished
def next_question():
    global current_question
    # Move to the next question
    current_question += 1

    # Check if there are more questions
    if current_question < len(quiz_data):
        # Display the next question
        show_question()
    else:
        # Display a message box with the final score and exit the application
        messagebox.showinfo("QUIZ COMPLETED",
                            "QUIZ COMPLETED! Final Score: {}/{}".format(score, len(quiz_data)))
        root.destroy()
