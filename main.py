from tkinter import *
from PIL import ImageTk,Image
import random
import time


root = Tk()
root.title("Dice Game")




#black border
d1_img = ImageTk.PhotoImage(Image.open("images/dice-six-faces-one.png"))
d2_img = ImageTk.PhotoImage(Image.open("images/dice-six-faces-two.png"))
d3_img = ImageTk.PhotoImage(Image.open("images/dice-six-faces-three.png"))
d4_img = ImageTk.PhotoImage(Image.open("images/dice-six-faces-four.png"))
d5_img = ImageTk.PhotoImage(Image.open("images/dice-six-faces-five.png"))
d6_img = ImageTk.PhotoImage(Image.open("images/dice-six-faces-six.png"))
#red border
r1_img = ImageTk.PhotoImage(Image.open("images/red-1.png"))
r2_img = ImageTk.PhotoImage(Image.open("images/red-2.png"))
r3_img = ImageTk.PhotoImage(Image.open("images/red-3.png"))
r4_img = ImageTk.PhotoImage(Image.open("images/red-4.png"))
r5_img = ImageTk.PhotoImage(Image.open("images/red-5.png"))
r6_img = ImageTk.PhotoImage(Image.open("images/red-6.png"))
#green border
g1 = ImageTk.PhotoImage(Image.open("images/green-1.png"))
g2 = ImageTk.PhotoImage(Image.open("images/green-2.png"))
g3 = ImageTk.PhotoImage(Image.open("images/green-3.png"))
g4 = ImageTk.PhotoImage(Image.open("images/green-4.png"))
g5 = ImageTk.PhotoImage(Image.open("images/green-5.png"))
g6 = ImageTk.PhotoImage(Image.open("images/green-6.png"))

#nums
num1_img = ImageTk.PhotoImage(Image.open("images/num-1.png"))
num2_img = ImageTk.PhotoImage(Image.open("images/num-2.png"))
num3_img = ImageTk.PhotoImage(Image.open("images/num-3.png"))


#other
dice_img = ImageTk.PhotoImage(Image.open("images/rolling-dice-cup.png"))
rolling_img = ImageTk.PhotoImage(Image.open("images/rolling-dices.png"))
perspective_rolling_img = ImageTk.PhotoImage(Image.open("images/perspective-dice-six-faces-random.png"))


 
dice_list = [d1_img, d2_img, d3_img, d4_img, d5_img, d6_img]
red_dice_list = [r1_img, r2_img, r3_img, r4_img, r5_img, r6_img]
green_dice_list = [g1, g2, g3, g4, g5, g6]

#top line
top_you = Label(root, text="YOU",font=('Times', 24))
top_you.grid(row=0, column=0)
top_pc = Label(root, text="PC",font=('Times', 24))
top_pc.grid(row=0, column=1)



#side YOU
image_you = Label(image=dice_img)
image_you.grid(row=1, column=0)

#side PC
image_pc = Label(image=dice_img)
image_pc.grid(row=1, column=1)

global won
global lost
won = 0
lost = 0

def num2():
    global image_pc
    global ranyou
    image_pc.grid_forget()
    image_pc = Label(image=num2_img)
    image_pc.grid(row=1, column=1)
    #num 3
    image_pc.after(1000, num1)

def num1():
    global image_pc
    global ranyou
    image_pc.grid_forget()
    image_pc = Label(image=num1_img)
    image_pc.grid(row=1, column=1)
    #dice
    image_pc.after(1000, pcLast)
    
    
    
    

def pcLast():
    global image_pc
    global ranyou
    global won
    global lost
    ranPc = random.randrange(0,5)
    image_pc.grid_forget()
    
    
    
    if ranyou == ranPc:
        image_pc = Label(image=green_dice_list[ ranPc ])
        result = Label(text="YOU WON",font=('Times', 36), background="#8fce00")
        won = won + 1
    else:
        image_pc = Label(image=red_dice_list[ ranPc ])
        result = Label(text="YOU LOST",font=('Times', 36), background="#f44336")
        lost = lost + 1
        
    image_pc.grid(row=1, column=1)
    result.grid(row=3, column=0,sticky='ew')
    
    score_won = Label(text="%d"%won,font=('Times', 36), foreground="#8fce00")
    score_lost = Label(text="%d"%lost,font=('Times', 36), foreground="#f44336")
    
    #delete score
    score_won.grid_forget()
    score_lost.grid_forget()
    
    #write score
    score_won.grid(row=3, column=1, columnspan=1, sticky='e')
    score_lost.grid(row=3, column=2, columnspan=1, sticky='w',)
   
 







def button_play():
    global image_you
    global image_pc
    global ranyou
    
    #You side
    ranYou = random.randrange(0,5)
    ranyou = ranYou
    
    image_you.grid_forget()
    image_you = Label(image=dice_list[ ranYou ])
    image_you.grid(row=1, column=0)
    #PC side
    #num3
    image_pc = Label(image=num3_img)
    image_pc.grid(row=1, column=1)
    
    #num2
    image_pc.after(1000, num2)
    
    
       
    
#buttons
button_quit = Button(root, text="Exit Game", command=root.quit)
button_play = Button(root, text="Play", command=button_play)

#buttons place
button_play.grid(row=2,column=0)
button_quit.grid(row=2,column=1)

root.mainloop()