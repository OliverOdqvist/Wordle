import tkinter as tk

root = tk.Tk()

root.title("Wordle")



canvas = tk.Canvas(root, width=1000, height=700)
canvas.grid(row=0)


tiles = {}
wordOfDay = "APPLE"

rowNum = 1
colNum = 1
xCoordinate = 240
yCoordinate = 20
for i in range(30):  # Adjusted from 30 to 36 for 6 rows * 5 columns = 36 tiles
    keyName = "row" + str(rowNum) + "_col" + str(colNum)
    square_size = 100  # Define the size of the square
    square = canvas.create_rectangle(xCoordinate, yCoordinate, xCoordinate + square_size, yCoordinate + square_size)
    tiles[keyName] = [xCoordinate + 50, yCoordinate + 50]
    xCoordinate += 110  # Adjusted the x-coordinate increment
    colNum += 1

    if colNum > 5:  # Check if we need to start a new row
        colNum = 1
        rowNum += 1
        xCoordinate = 240  # Reset x-coordinate for the new row
        yCoordinate += 110  # Adjusted the y-coordinate increment for the new row

currentTile = tiles["row1_col1"]
colInRow = 1
row = 1
inputs = {}
currentWord = ""              #Current word the user is guessing

def pressedEnter():
    global colInRow
    global row
    if colInRow == 6:    #Checking to make sure user has put a character in each box on a row
        if currentWord == wordOfDay:         #If word of the day is the same as what the user has inputted they win
            return "YIPEE!!!"
        else:
            if row < 6:                      #Checking to make sure user not on final row
                colInRow = 1                 #Setting program back so that when user gives next character its placed in first box on row
                row = row + 1                #Selecting the next row
                return colInRow, row

def pressedBack(): 
    global colInRow
    global currentWord
    if colInRow >= 2:             #Checking whether a character has been inputted in row yet 
        key = "row" + str(row) + "_" + "col" + (str(colInRow - 1))
        canvas.delete(inputs[key])
        del inputs[key]
        colInRow -= 1
        currentWord = currentWord[:-1]          #remove final letter from current word user is guessing


def input_letter(letter):
    global colInRow
    global currentWord
    if colInRow <= 5:
        key = "row" + str(row) + "_" + "col" + str(colInRow)
        char = canvas.create_text(tiles[key][0], tiles[key][1], text=f"{letter}", font=("Helvetica", "50", "bold"))
        inputs[key] = char
        colInRow = colInRow + 1
        currentWord += letter          #Add letter of button clicked to word user is guessing
    

letters = tk.Frame(root)
letters.grid(row=1)  

qBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="Q", command=lambda: input_letter("Q"))
qBtn.grid(row=0, column=0)

wBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="W", command=lambda: input_letter("W"))
wBtn.grid(row=0, column=1)

eBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="E", command=lambda: input_letter("E"))
eBtn.grid(row=0, column=2)

rBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="R", command=lambda: input_letter("R"))
rBtn.grid(row=0, column=3)

tBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="T", command=lambda: input_letter("T"))
tBtn.grid(row=0, column=4)

yBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="Y", command=lambda: input_letter("Y"))
yBtn.grid(row=0, column=5)

uBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="U", command=lambda: input_letter("U"))
uBtn.grid(row=0, column=6)

iBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="I", command=lambda: input_letter("I"))
iBtn.grid(row=0, column=7)

oBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="O", command=lambda: input_letter("O"))
oBtn.grid(row=0, column=8)

pBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="P", command=lambda: input_letter("P"))
pBtn.grid(row=0, column=9)

aBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="A", command=lambda: input_letter("A"))
aBtn.grid(row=1, column=0)

sBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="S", command=lambda: input_letter("S"))
sBtn.grid(row=1, column=1)

dBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="D", command=lambda: input_letter("D"))
dBtn.grid(row=1, column=2)

fBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="F", command=lambda: input_letter("F"))
fBtn.grid(row=1, column=3)

gBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="G", command=lambda: input_letter("G"))
gBtn.grid(row=1, column=4)

hBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="H", command=lambda: input_letter("H"))
hBtn.grid(row=1, column=5)

jBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="J", command=lambda: input_letter("J"))
jBtn.grid(row=1, column=6)

kBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="K", command=lambda: input_letter("K"))
kBtn.grid(row=1, column=7)

lBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="L", command=lambda: input_letter("L"))
lBtn.grid(row=1, column=8)

enterBtn = tk.Button(letters, bg="ivory3", height=3, width=6, text="ENTER", command=pressedEnter)
enterBtn.grid(row=2, column=0)

zBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="Z", command=lambda: input_letter("Z"))
zBtn.grid(row=2, column=1)

xBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="X", command=lambda: input_letter("X"))
xBtn.grid(row=2, column=2)

cBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="C", command=lambda: input_letter("C"))
cBtn.grid(row=2, column=3)

vBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="V", command=lambda: input_letter("V"))
vBtn.grid(row=2, column=4)

bBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="B", command=lambda: input_letter("B"))
bBtn.grid(row=2, column=5)

nBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="N", command=lambda: input_letter("N"))
nBtn.grid(row=2, column=6)

mBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="M", command=lambda: input_letter("M"))
mBtn.grid(row=2, column=7)

backspaceBtn = tk.Button(letters, bg="ivory3", height=3, width=6, text="DELETE", command=pressedBack)
backspaceBtn.grid(row=2, column=8)

root.mainloop()
