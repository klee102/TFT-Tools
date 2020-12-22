import matchupList as mu
from tkinter import *
from tkinter.font import Font

root = Tk()
root.geometry("800x600")

frame1 = Frame(root)
frame1.pack(side=LEFT)

frame2 = Frame(root)
frame2.pack()

frame3 = Frame(root)
frame3.pack()

#functions------------------------------------------------------------------------

def updateNames():
    namePlayerA.set(entryA.get())
    namePlayerB.set(entryB.get())
    namePlayerC.set(entryC.get())
    namePlayerD.set(entryD.get())
    namePlayerE.set(entryE.get())
    namePlayerF.set(entryF.get())
    namePlayerG.set(entryG.get())

def updateMatchHistory(name):

    matchHistory.append(name)

    if len(matchHistory) > possiblePlayerCount[otherPlayersAlive]:
        matchHistory.pop(0)

    clearHistoryAndOpponents()

    for i in matchHistory:
        matchHistoryText.insert(END, i.get() + "\n")
        
    for j in playerList:
        if j not in matchHistory:
            possibleOpponentsText.insert(END, j.get() + "\n")

def eliminatePlayer():
    #set command for each button to disable it after button press
    #after button press, set each button's command (besides disabled one) 
    # to update match history again

    playerA.config(command=lambda: playerA.config(state=DISABLED))
    playerB.config(command=lambda: playerB.config(state=DISABLED))
    playerC.config(command=lambda: playerC.config(state=DISABLED))
    playerD.config(command=lambda: playerD.config(state=DISABLED))
    playerE.config(command=lambda: playerE.config(state=DISABLED))
    playerF.config(command=lambda: playerF.config(state=DISABLED))
    playerG.config(command=lambda: playerG.config(state=DISABLED))  

    doneButton.grid(row=1, column=3)

def restoreCommand():
    playerA.config(command=lambda: updateMatchHistory(namePlayerA))
    playerB.config(command=lambda: updateMatchHistory(namePlayerB))
    playerC.config(command=lambda: updateMatchHistory(namePlayerC))
    playerD.config(command=lambda: updateMatchHistory(namePlayerD))
    playerE.config(command=lambda: updateMatchHistory(namePlayerE))
    playerF.config(command=lambda: updateMatchHistory(namePlayerF))
    playerG.config(command=lambda: updateMatchHistory(namePlayerG))

    clearHistoryAndOpponents()

    doneButton.grid_forget()

def chooseDisabledButton():
    playerA.config(state=DISABLED)

def clearHistoryAndOpponents():
    global matchHistory
    matchHistory = []

    global potentialOpponents
    potentialOpponents = []

def reset():
    namePlayerA.set("A")
    namePlayerB.set("B")
    namePlayerC.set("C")
    namePlayerD.set("D")
    namePlayerE.set("E")
    namePlayerF.set("F")
    namePlayerG.set("G")

    for i in [entryA, entryB, entryC, entryD, entryE, entryF, entryG]:
        i.delete(0, END)

    clearHistoryAndOpponents()

    playerA.config(state=NORMAL)
    playerB.config(state=NORMAL)
    playerC.config(state=NORMAL)
    playerD.config(state=NORMAL)
    playerE.config(state=NORMAL)
    playerF.config(state=NORMAL)
    playerG.config(state=NORMAL)

    restoreCommand()

    
#instantiate data-----------------------------------------------------------------

namePlayerA = StringVar()
namePlayerA.set("A")
namePlayerB = StringVar()
namePlayerB.set("B")
namePlayerC = StringVar()
namePlayerC.set("C")
namePlayerD = StringVar()
namePlayerD.set("D")
namePlayerE = StringVar()
namePlayerE.set("E")
namePlayerF = StringVar()
namePlayerF.set("F")
namePlayerG = StringVar()
namePlayerG.set("G")

playerList = [namePlayerA,\
    namePlayerB,\
    namePlayerC,\
    namePlayerD,\
    namePlayerE,\
    namePlayerF,\
    namePlayerG,\
    ]
possiblePlayerCount = {7:4, 6:3, 5:2, 4:1, 3:1}
otherPlayersAlive = 7
matchHistory = []
potentialOpponents = []

# player buttons--------------------------------------------------------
playerA = Button(frame1, textvariable = namePlayerA, width=10, height=5,\
    command=lambda: updateMatchHistory(namePlayerA))
    
playerA.grid(row=0, column=0)

playerB = Button(frame1, textvariable = namePlayerB, width=10, height=5,\
    command=lambda: updateMatchHistory(namePlayerB))
playerB.grid(row=0, column=1)

playerC = Button(frame1, textvariable = namePlayerC, width=10, height=5,\
    command=lambda: updateMatchHistory(namePlayerC))
playerC.grid(row=0, column=2)

playerD = Button(frame1, textvariable = namePlayerD, width=10, height=5,\
    command=lambda: updateMatchHistory(namePlayerD))
playerD.grid(row=0, column=3)

playerE = Button(frame1, textvariable = namePlayerE, width=10, height=5,\
    command=lambda: updateMatchHistory(namePlayerE))
playerE.grid(row=1, column=0)

playerF = Button(frame1, textvariable = namePlayerF, width=10, height=5,\
    command=lambda: updateMatchHistory(namePlayerF))
playerF.grid(row=1, column=1)

playerG = Button(frame1, textvariable = namePlayerG, width=10, height=5,\
    command=lambda: updateMatchHistory(namePlayerG))
playerG.grid(row=1, column=2)


# Labels---------------------------------------------------------------------------

matchHistoryHeader = Label(frame2, text="Match History",\
     font=Font(family='Helvetica', size=12, underline=1))
matchHistoryHeader.grid(row=0, column=2)

matchHistoryText = Text(frame2, width=25, height=8)
matchHistoryText.grid(row=1, column=2)

possibleOpponentsHeader = Label(frame2, text = "Possible Opponents",\
    font=Font(family='Helvetica', size=12, underline=1))
possibleOpponentsHeader.grid(row=2, column=2)

possibleOpponentsText = Text(frame2, width=25, height=8)
possibleOpponentsText.grid(row=3, column=2)


#Buttons--------------------------------------------------------------------------
eliminatePlayerButton = Button(frame2, text = "Eliminate Player", width=20, command=eliminatePlayer)
eliminatePlayerButton.grid(row=4, column=2)

resetButton = Button(frame2, text = "Reset All", width=20, command=reset)
resetButton.grid(row=5, column=2)

doneButton = Button(frame1, text = "Done", width=10, height=5, command=restoreCommand)
doneButton.grid(row=1, column=3)
doneButton.grid_forget()

# entry header + bars---------------------------------------------------

entryHeader = Label(frame3, text="Enter Players Below:", \
    font=Font(family='Helvetica', size=12, underline=1)).grid(row=0)

entryA = Entry(frame3)
entryA.grid(row=1)
entryB = Entry(frame3)
entryB.grid(row=2)
entryC = Entry(frame3)
entryC.grid(row=3)
entryD = Entry(frame3)
entryD.grid(row=4)
entryE = Entry(frame3)
entryE.grid(row=5)
entryF = Entry(frame3)
entryF.grid(row=6)
entryG = Entry(frame3)
entryG.grid(row=7)

updateNames = Button(frame3, text="Update Names", command=updateNames).grid(row=8)

root.title("Matchup Handler")
root.mainloop()
