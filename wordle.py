import tkinter as tk
import datetime as dt
import requests

root = tk.Tk()

root.title("Wordle")



canvas = tk.Canvas(root, width=1000, height=700)
canvas.grid(row=0)


tiles = {}                   #Dictionary to store each tile in grid
changeTiles = {}
dayTotalOccurence = {}           #Dictionary to map the ammount of occurences of a letter in the word of the day

#Getting current word of day from wordle
currentDate = dt.date.today()       #Current date which is needed in order to access ocrrect json
url = f"https://www.nytimes.com/svc/wordle/v2/{currentDate:%Y-%m-%d}.json"      #link to the json file containing current word
query = requests.get(url).json()       #Querying for word
wordOfDay = query["solution"].upper()   #Current word of the day

def mapWordOfDayOccurences():
    for elt in wordOfDay:            #Maps number of occurences of letters in word of the day in a dictionary
        if elt in dayTotalOccurence:
            dayTotalOccurence[elt] += 1
        else:
            dayTotalOccurence[elt] = 1

mapWordOfDayOccurences()

def createGrid():
    rowNum = 1
    colNum = 1
    xCoordinate = 240
    yCoordinate = 20
    for i in range(30):  # Adjusted from 30 to 36 for 6 rows * 5 columns = 36 tiles
        keyName = "row" + str(rowNum) + "_col" + str(colNum)
        square_size = 100  # Define the size of the square
        square = canvas.create_rectangle(xCoordinate, yCoordinate, xCoordinate + square_size, yCoordinate + square_size)

        tiles[keyName] = [xCoordinate + 50, yCoordinate + 50]
        changeTiles[keyName] = square
        xCoordinate += 110  # Adjusted the x-coordinate increment
        colNum += 1

        if colNum > 5:  # Check if we need to start a new row
            colNum = 1
            rowNum += 1
            xCoordinate = 240  # Reset x-coordinate for the new row
            yCoordinate += 110  # Adjusted the y-coordinate increment for the new row

createGrid()
currentTile = tiles["row1_col1"]
colInRow = 1
row = 1
inputs = {}
currentWord = ""              #Current word the user is guessing

def turnGreen(currentTile, dic, elt):         #Function to turn letter box green
    if dic.get(elt, 0) == 0:          #Checking to see if letter in guess occurs in dictionary yet or not, if it hasn't then add it as occuring once
        dic[elt] = 1
    else:                       #If it already occurs then add one to the total occurences for that letter
        dic[elt] += 1
    canvas.itemconfig(changeTiles[currentTile], fill="green")
    return dic

def turnOrange(currentTile, dic, elt): #Same as previous function but to turn letter box orange for correct letter but not correct position
    if dic.get(elt, 0) == 0:
        dic[elt] = 1
    else:
        dic[elt] += 1
    canvas.itemconfig(changeTiles[currentTile], fill="orange")
    return dic

def pressedEnter(e=""):     #default parameter for .bind()
    global colInRow
    global row
    global currentWord
    global wordOfDay
    if colInRow == 6:    #Checking to make sure user has put a character in each box on a row
        if currentWord == wordOfDay:         #If word of the day is the same as users guess
            print("YIPEE!!!")
        else:
            currentTotalOccurence = {}       #Dictionary which maps the total occurence of a letter to that letter a the key
            for currIndex, currChar in enumerate(currentWord):
                for dayIndex, dayChar in enumerate(wordOfDay):
                    if currChar == dayChar and currIndex == dayIndex:            #If a letter is in the guess and in the correct position turn green
                        if currentTotalOccurence.get(currChar, 0) < dayTotalOccurence[currChar]:   #Checking to see if letter features same amount in guess than word of day's letter occurence dictionary
                            tile = "row" + str(row) + "_col" + str(currIndex + 1)
                            turnGreen(tile, currentTotalOccurence, currChar)                       #Turns tile green
                    elif currChar == dayChar and currIndex != dayIndex:
                        if currentTotalOccurence.get(currChar, 0) < dayTotalOccurence[currChar]:
                            tile = "row" + str(row) + "_col" + str(currIndex + 1)
                            turnOrange(tile, currentTotalOccurence, currChar)
            if row < 6:                      #Checking to make sure user not on final row
                colInRow = 1                 #Setting program back so that when user gives next character its placed in first box on row
                row = row + 1                #Selecting the next row
                currentWord = ""
                return colInRow, row

def pressedBack(e=""): #Default parameter for .bind() 
    global colInRow
    global currentWord
    if colInRow >= 2:             #Checking whether a character has been inputted in row yet 
        key = "row" + str(row) + "_" + "col" + (str(colInRow - 1))
        canvas.delete(inputs[key])
        del inputs[key]
        colInRow -= 1
        currentWord = currentWord[:-1]          #remove final letter from current word user is guessing


def input_letter(letter):    #Function takes either on screen keyboard press as argument or .bind() 
    if type(letter) != str:        #Checks if .bind() called the function
        if not letter.char.isalpha():       #If character is not a letter ignore it
            return
    global colInRow
    global currentWord
    if colInRow <= 5:
        key = "row" + str(row) + "_" + "col" + str(colInRow)
        if type(letter) == str:         #Checking if argument was sent by .bind() or on screen keyboard
            char = canvas.create_text(tiles[key][0], tiles[key][1], text=f"{letter}", font=("Helvetica", "50", "bold"))
            currentWord += letter          #Add letter of button clicked to word user is guessing
        else:
            currentWord += letter.char.upper()          #Add letter from key user clicked on keyboard and capitalise it
            char = canvas.create_text(tiles[key][0], tiles[key][1], text=f"{letter.char.upper()}", font=("Helvetica", "50", "bold"))
        inputs[key] = char
        colInRow = colInRow + 1
    
#Create keyboard on screen
letters = tk.Frame(root)
letters.grid(row=1)
keyboard = {}

qBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="Q", command=lambda: input_letter("Q"))
qBtn.grid(row=0, column=0)
keyboard["q"] = qBtn

wBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="W", command=lambda: input_letter("W"))
wBtn.grid(row=0, column=1)
keyboard["w"] = wBtn

eBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="E", command=lambda: input_letter("E"))
eBtn.grid(row=0, column=2)
keyboard["e"] = eBtn

rBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="R", command=lambda: input_letter("R"))
rBtn.grid(row=0, column=3)
keyboard["r"] = rBtn

tBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="T", command=lambda: input_letter("T"))
tBtn.grid(row=0, column=4)
keyboard["t"] = tBtn

yBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="Y", command=lambda: input_letter("Y"))
yBtn.grid(row=0, column=5)
keyboard["y"] = yBtn

uBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="U", command=lambda: input_letter("U"))
uBtn.grid(row=0, column=6)
keyboard["u"] = uBtn

iBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="I", command=lambda: input_letter("I"))
iBtn.grid(row=0, column=7)
keyboard["i"] = iBtn

oBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="O", command=lambda: input_letter("O"))
oBtn.grid(row=0, column=8)
keyboard["o"] = oBtn

pBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="P", command=lambda: input_letter("P"))
pBtn.grid(row=0, column=9)
keyboard["p"] = pBtn

aBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="A", command=lambda: input_letter("A"))
aBtn.grid(row=1, column=0)
keyboard["a"] = aBtn

sBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="S", command=lambda: input_letter("S"))
sBtn.grid(row=1, column=1)
keyboard["s"] = sBtn

dBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="D", command=lambda: input_letter("D"))
dBtn.grid(row=1, column=2)
keyboard["d"] = dBtn

fBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="F", command=lambda: input_letter("F"))
fBtn.grid(row=1, column=3)
keyboard["f"] = fBtn

gBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="G", command=lambda: input_letter("G"))
gBtn.grid(row=1, column=4)
keyboard["g"] = gBtn

hBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="H", command=lambda: input_letter("H"))
hBtn.grid(row=1, column=5)
keyboard["h"] = hBtn

jBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="J", command=lambda: input_letter("J"))
jBtn.grid(row=1, column=6)
keyboard["j"] = jBtn

kBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="K", command=lambda: input_letter("K"))
kBtn.grid(row=1, column=7)
keyboard["k"] = kBtn

lBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="L", command=lambda: input_letter("L"))
lBtn.grid(row=1, column=8)
keyboard["l"] = lBtn

enterBtn = tk.Button(letters, bg="ivory3", height=3, width=6, text="ENTER", command=pressedEnter)
enterBtn.grid(row=2, column=0)
keyboard["enter"] = enterBtn

zBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="Z", command=lambda: input_letter("Z"))
zBtn.grid(row=2, column=1)
keyboard['z'] = zBtn

xBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="X", command=lambda: input_letter("X"))
xBtn.grid(row=2, column=2)
keyboard["x"] = xBtn

cBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="C", command=lambda: input_letter("C"))
cBtn.grid(row=2, column=3)
keyboard["c"] = cBtn

vBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="V", command=lambda: input_letter("V"))
vBtn.grid(row=2, column=4)
keyboard["v"] = vBtn

bBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="B", command=lambda: input_letter("B"))
bBtn.grid(row=2, column=5)
keyboard["b"] = bBtn

nBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="N", command=lambda: input_letter("N"))
nBtn.grid(row=2, column=6)
keyboard["n"] = nBtn

mBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="M", command=lambda: input_letter("M"))
mBtn.grid(row=2, column=7)
keyboard["m"] = mBtn

backspaceBtn = tk.Button(letters, bg="ivory3", height=3, width=6, text="DELETE", command=pressedBack)
backspaceBtn.grid(row=2, column=8)
keyboard["backspace"] = backspaceBtn

#Functionality for keyboard input
#Checks for any letter being pressed
root.bind("<KeyPress>", input_letter)

#Checks for backspace being pressed
root.bind("<BackSpace>", pressedBack)

#Checks for return being pressed
root.bind("<Return>", pressedEnter)

root.mainloop()
