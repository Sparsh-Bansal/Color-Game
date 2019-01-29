from tkinter import *
import random

colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
timeleft = 30

def startGame(event):
    if timeleft == 30:
        countdown()
    nextColour()

def nextColour():
    global score
    global timeleft
    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1

        e.delete(0,END)

        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Score: " + str(score))

def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: "
                              + str(timeleft))
        timeLabel.after(1000, countdown)

root = Tk()
root.title("COLOR GAME")
root.geometry("375x260")
instructions = Label(root, text="Type in the colour "
                                        "of the words, and not the word text!",
                             font=('Helvetica', 12),bg="light yellow",fg="red",pady=10)
instructions.pack()
scoreLabel = Label(root, text="Press ENTER to Start the Game",
                           font=('Helvetica', 12),bg="light green",fg="green",padx=20,pady=10)
scoreLabel.pack()
timeLabel = Label(root, text="Time left: " +
                                     str(timeleft), font=('Helvetica', 20),pady=10)
timeLabel.pack()
label = Label(root, font=('Helvetica', 60))
label.pack()
e = Entry(root,width=50,justify=CENTER)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()
root.mainloop()
