from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font
import itemCombinations as iC

#create a new function or file that looks at completed items
#and suggests comps to play based on those items
#e.g. if blue buff and morello in completedItems:
#errorMsg.set("could be viktor mech or astro snipers")
#e.g. if 3 bows in completedItems:
#errorMsg.set("bang bros? yi carry?")

root = Tk()
root.geometry("1280x720")
frame = Frame(root)
frame.pack()

topFrame = Frame(root)
topFrame.pack(side=TOP)

leftFrame = Frame(root)
leftFrame.pack(side=LEFT)

#quant and list initialization------------------------------------------------
itemString = ""

beltQuant = IntVar()
beltQuant.set(0)

bowQuant = IntVar()
bowQuant.set(0)

cloakQuant = IntVar()
cloakQuant.set(0)

gloveQuant = IntVar()
gloveQuant.set(0)

rodQuant = IntVar()
rodQuant.set(0)

swordQuant = IntVar()
swordQuant.set(0)

tearQuant = IntVar()
tearQuant.set(0)

vestQuant = IntVar()
vestQuant.set(0)

spatQuant = IntVar()
spatQuant.set(0)

completableItemsLabel = StringVar()
completableItemsLabel.set("Completable Items")
completableItemsLabel = Label(leftFrame, textvariable = completableItemsLabel)
completableItemsLabel.grid(row=0, column=0)

errorMsg = StringVar()
errorMsg.set("")
errorStr = Label(topFrame, textvariable=errorMsg)
errorStr.grid(row=6, columnspan = 9)

#belt-------------------------------------------------------------------------

beltIcon = Image.open("icons/belt.png")
beltRender = ImageTk.PhotoImage(beltIcon)
beltImg = Label(topFrame, image=beltRender).grid(row=1, column=0)

beltQuantBox = Spinbox(topFrame, from_= 0, to = 8, width=5, \
    font=Font(family='Helvetica', size=12), justify=CENTER)
beltQuantBox.grid(row=2, column=0)

#bow-------------------------------------------------------------------------

bowIcon = Image.open("icons/bow.png")
bowRender = ImageTk.PhotoImage(bowIcon)
bowImg = Label(topFrame, image=bowRender).grid(row=1, column=1)

bowQuantBox = Spinbox(topFrame, from_= 0, to = 8, width=5, \
    font=Font(family='Helvetica', size=12), justify=CENTER)
bowQuantBox.grid(row=2, column=1)

#cloak-------------------------------------------------------------------------

cloakIcon = Image.open("icons/cloak.png")
cloakRender = ImageTk.PhotoImage(cloakIcon)
cloakImg = Label(topFrame, image=cloakRender).grid(row=1, column=2)

cloakQuantBox = Spinbox(topFrame, from_= 0, to = 8, width=5, \
    font=Font(family='Helvetica', size=12), justify=CENTER)
cloakQuantBox.grid(row=2, column=2)

#glove-------------------------------------------------------------------------

gloveIcon = Image.open("icons/glove.png")
gloveRender = ImageTk.PhotoImage(gloveIcon)
gloveImg = Label(topFrame, image=gloveRender).grid(row=1, column=3)

gloveQuantBox = Spinbox(topFrame, from_= 0, to = 8, width=5, \
    font=Font(family='Helvetica', size=12), justify=CENTER)
gloveQuantBox.grid(row=2, column=3)

#rod-------------------------------------------------------------------------

rodIcon = Image.open("icons/rod.png")
rodRender = ImageTk.PhotoImage(rodIcon)
rodImg = Label(topFrame, image=rodRender).grid(row=1, column=4)

rodQuantBox = Spinbox(topFrame, from_= 0, to = 8, width=5, \
    font=Font(family='Helvetica', size=12), justify=CENTER)
rodQuantBox.grid(row=2, column=4)

#sword-------------------------------------------------------------------------

swordIcon = Image.open("icons/sword.png")
swordRender = ImageTk.PhotoImage(swordIcon)
swordImg = Label(topFrame, image=swordRender).grid(row=1, column=5)

swordQuantBox = Spinbox(topFrame, from_= 0, to = 8, width=5, \
    font=Font(family='Helvetica', size=12), justify=CENTER)
swordQuantBox.grid(row=2, column=5)

#tear-------------------------------------------------------------------------

tearIcon = Image.open("icons/tear.png")
tearRender = ImageTk.PhotoImage(tearIcon)
tearImg = Label(topFrame, image=tearRender).grid(row=1, column=6)

tearQuantBox = Spinbox(topFrame, from_= 0, to = 8, width=5, \
    font=Font(family='Helvetica', size=12), justify=CENTER)
tearQuantBox.grid(row=2, column=6)

#vest-------------------------------------------------------------------------

vestIcon = Image.open("icons/vest.png")
vestRender = ImageTk.PhotoImage(vestIcon)
vestImg = Label(topFrame, image=vestRender).grid(row=1, column=7)

vestQuantBox = Spinbox(topFrame, from_= 0, to = 8, width=5, \
    font=Font(family='Helvetica', size=12), justify=CENTER)
vestQuantBox.grid(row=2, column=7)

#spatula-------------------------------------------------------------------------

spatIcon = Image.open("icons/spatula.png")
spatRender = ImageTk.PhotoImage(spatIcon)
spatImg = Label(topFrame, image=spatRender).grid(row=1, column=8)

spatQuantBox = Spinbox(topFrame, from_= 0, to = 8, width=5, \
    font=Font(family='Helvetica', size=12), justify=CENTER)
spatQuantBox.grid(row=2, column=8)

#functions--------------------------------------------------------------------

def intCheck(data):
    try:
        data = int(data)

    except:
        data = 0
        errorMsg.set("Invalid entry. Check your inputs again.")

    return data

def updateItems():

    for widget in leftFrame.winfo_children():
        widget.destroy()

    completableItemsLabel = StringVar()
    completableItemsLabel.set("Completable Items")
    completableItemsLabel = Label(leftFrame, textvariable = completableItemsLabel)
    completableItemsLabel.grid(row=0, column=0) 

    beltQuant = intCheck(beltQuantBox.get())
    bowQuant = intCheck(bowQuantBox.get())
    cloakQuant = intCheck(cloakQuantBox.get())
    gloveQuant = intCheck(gloveQuantBox.get())
    rodQuant = intCheck(rodQuantBox.get())
    swordQuant = intCheck(swordQuantBox.get())
    tearQuant = intCheck(tearQuantBox.get())
    vestQuant = intCheck(vestQuantBox.get())    
    spatQuant = intCheck(spatQuantBox.get())

    itemString = \
        "Belt, " * beltQuant \
        + "Bow, " * bowQuant \
        + "Cloak, " * cloakQuant \
        + "Glove, " * gloveQuant \
        + "Rod, " * rodQuant \
        + "Sword, " * swordQuant \
        + "Tear, " * tearQuant \
        + "Vest, " * vestQuant \
        + "Spatula, " * spatQuant

    itemString = iC.cleanItemString(itemString)
    completedItems = iC.removeDuplicateItems(\
                        iC.makeCompletedItems((itemString)))
    
    #word wrap but with the icons / names
    c = 0
    r = 1
    for i in completedItems:
        
        tempStr = "icons/" + i + ".png"
        tempIcon = Image.open(tempStr)
        tempRender = ImageTk.PhotoImage(tempIcon)
        tempImg = Label(leftFrame, image=tempRender)
        tempImg.image = tempRender
        tempImg.grid(row=r, column=c)
       
        Label(leftFrame, text = i, width=15).grid(row=r+1,column=c)
        c = c + 1
        if c > 6:
            r += 2
            c = 0

    if "Blue Buff" in completedItems:
        errorMsg.set("SLAM THE BLUE BUFF POG")

def resetItems():
    beltQuantBox.delete(0, "end")
    beltQuantBox.insert(0, "0")

    bowQuantBox.delete(0, "end")
    bowQuantBox.insert(0, "0")

    cloakQuantBox.delete(0, "end")
    cloakQuantBox.insert(0, "0")
    
    gloveQuantBox.delete(0, "end")
    gloveQuantBox.insert(0, "0")

    rodQuantBox.delete(0, "end")
    rodQuantBox.insert(0, "0")

    swordQuantBox.delete(0, "end")
    swordQuantBox.insert(0, "0")

    tearQuantBox.delete(0, "end")
    tearQuantBox.insert(0, "0")

    vestQuantBox.delete(0, "end")
    vestQuantBox.insert(0, "0")

    spatQuantBox.delete(0, "end")
    spatQuantBox.insert(0, "0")

    errorMsg.set("")

    updateItems()

#update button---------------------------------------------------------------

updateButton = Button(topFrame, text="Update", command=updateItems, width = 85)
updateButton.grid(row=4, columnspan=9)

#reset button----------------------------------------------------------------

resetButton = Button(topFrame, text="Reset", command = resetItems, width = 85)
resetButton.grid(row=5, columnspan=9)

root.title("TFT Item Combinations GUI")
root.mainloop()