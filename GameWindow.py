from tkinter import *



#root = Tk()
#topFrame = Frame(root)
#topFrame.pack()
#bottomFrame = Frame(root)
#bottomFrame.pack(side=BOTTOM)
#rock = Button(bottomFrame, text = "rock")
#paper = Button(bottomFrame, text = "paper")
#scissors = Button(bottomFrame, text = "scissors")
#greetingLabel = Label(topFrame, text="Let's play! Click your pick:    ")
#greetingLabel.pack(fill = X)
#rock.grid(row = 0, column = 0, sticky = W)
#paper.grid(row = 0, column = 1)
#scissors.grid(row = 0, column =2, sticky = E)
#root.mainloop()

class PlayWindow():
    root = Tk()

    topFrame = Frame(root)
    topFrame.pack()
    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)
    rock = Button(bottomFrame, text = "rock")
    paper = Button(bottomFrame, text = "paper")
    scissors = Button(bottomFrame, text = "scissors")
    greetingLabel = Label(topFrame, text="Let's play! Click your pick:    ")
    greetingLabel.pack(fill = X)
    rock.grid(row = 0, column = 0, sticky = W)
    paper.grid(row = 0, column = 1)
    scissors.grid(row = 0, column =2, sticky = E)
    root.mainloop()

window = PlayWindow()