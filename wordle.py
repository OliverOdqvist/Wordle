import tkinter as tk

root = tk.Tk()

root.title("Wordle")



canvas = tk.Canvas(root, width=1000, height=700)
canvas.grid(row=0)


tiles = {}

rowNum = 1
colNum = 1
xCoordinate = 240
yCoordinate = 0
rowCoordinate1 = 20
rowCoordinate2 = 0
for i in range(30):  # Adjusted from 30 to 36 for 6 rows * 5 columns = 36 tiles
    keyName = "row" + str(rowNum) + "_col" + str(colNum)
    square_size = 100  # Define the size of the square
    square = canvas.create_rectangle(xCoordinate, rowCoordinate1, xCoordinate + square_size, rowCoordinate1 + square_size)
    tiles[keyName] = square
    xCoordinate += 110  # Adjusted the x-coordinate increment
    colNum += 1

    if colNum > 5:  # Check if we need to start a new row
        colNum = 1
        rowNum += 1
        xCoordinate = 240  # Reset x-coordinate for the new row
        yCoordinate += 110  # Adjusted the y-coordinate increment for the new row
        rowCoordinate1 += 110  # Adjusted the y-coordinate increment for the new row
        rowCoordinate2 += 110  # Adjusted the y-coordinate increment for the new row

letters = tk.Frame(root)
letters.grid(row=1)  

qBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="Q")
qBtn.grid(row=0, column=0)

wBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="W")
wBtn.grid(row=0, column=1)

eBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="E")
eBtn.grid(row=0, column=2)

rBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="R")
rBtn.grid(row=0, column=3)

tBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="T")
tBtn.grid(row=0, column=4)

yBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="Y")
yBtn.grid(row=0, column=5)

uBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="U")
uBtn.grid(row=0, column=6)

iBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="I")
iBtn.grid(row=0, column=7)

oBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="O")
oBtn.grid(row=0, column=8)

pBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="P")
pBtn.grid(row=0, column=9)

aBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="P")
aBtn.grid(row=1, column=0)

sBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="S")
sBtn.grid(row=1, column=1)

dBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="D")
dBtn.grid(row=1, column=2)

fBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="F")
fBtn.grid(row=1, column=3)

gBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="G")
gBtn.grid(row=1, column=4)

hBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="H")
hBtn.grid(row=1, column=5)

jBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="J")
jBtn.grid(row=1, column=6)

kBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="K")
kBtn.grid(row=1, column=7)

lBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="L")
lBtn.grid(row=1, column=8)

zBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="Z")
zBtn.grid(row=2, column=1)

xBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="X")
xBtn.grid(row=2, column=2)

cBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="C")
cBtn.grid(row=2, column=3)

vBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="V")
vBtn.grid(row=2, column=4)

bBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="B")
bBtn.grid(row=2, column=5)

nBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="N")
nBtn.grid(row=2, column=6)

mBtn = tk.Button(letters, bg="ivory3", height=3, width=4, text="M")
mBtn.grid(row=2, column=7)

root.mainloop()