#imorting tkinter modules
from tkinter import *
from tkinter import messagebox
#creating a window
win = Tk()
#title of win
win.title("AP pong game")
#initializing a canvas area and making it ready
canvas = Canvas(width = 500, height = 320, bg = "turquoise")
canvas.grid(row = 0, column = 0)
#creating bat class
class bat:
    """creating bat class"""
    def __init__(self, x0, y0, x1, y1, color):
        #checking inputs
        if not isinstance(x0, int) or not isinstance(y0, int) or not isinstance(x1, int) or not isinstance(y1, int):
            messagebox.showinfo(title="Error", message = "Coordinates must be integer")
        if not isinstance(color, str):
            messagebox.showinfo(title="Error", message = "Color must be string")
        #rceating bat
        self.object = canvas.create_rectangle(x0, y0, x1, y1, fill = color)

    # move bat
    def move_bat(self, event):
        if event.keysym == 'Right':
            canvas.move(self.object, 10, 0)
        elif event.keysym == 'Left':
            canvas.move(self.object, -10, 0)
    def finalizing (self):
        canvas.bind_all('<Right>', self.move_bat)
        canvas.bind_all('<Left>', self.move_bat)


#creating ball class
class ball:
    """in this class we build ball""" 
    gameover = False

    def __init__(self, x0: int, y0: int, x1: int, y1: int, color: str, Bat: bat):
        #checking inputs
        if not isinstance(x0, int) or not isinstance(y0, int) or not isinstance(x1, int) or not isinstance(y1, int):
            messagebox.showinfo(title="Error", message = "Coordinates must be integer")
        if not isinstance(color, str):
            messagebox.showinfo(title="Error", message = "Color must be string")
        #creating ball on canvas
        self.moving_object = canvas.create_oval(x0, y0, x1, y1, fill = color)
        #assigning bat
        self.bat = Bat
        self.deltax = 3
        self.deltay = 3
        

    def moveball (self):
        canvas.move(self.moving_object, self.deltax, self.deltay)
        ball_pos=canvas.coords(self.moving_object)
        bat_pos=canvas.coords(self.bat.object)
        if ball_pos[2] >= bat_pos[0] and ball_pos[0] <= bat_pos[2]: 
            if ball_pos[3] >= bat_pos[1] and ball_pos[3] <= bat_pos[3]:
                self.deltay = -3
        if ball_pos[0] <= 0:
            self.deltax = 3
        if ball_pos[2] >= 500:
            self.deltax = -3

        if ball_pos[1] <= 0:
            self.deltay = 3

        if ball_pos[3] >= 320:
            messagebox.showinfo(title = "GAVE OVER", message = "you Lost")
            ball.gameover = True
            win.destroy()

        if not ball.gameover:
            canvas.after(30, self.moveball)
        
    def finalizing(self) :   
        canvas.after(30, self.moveball)

            
bat1 = bat(0, 310, 100, 320, "blue")
ball1 = ball(30, 30, 50, 50, "yellow", bat1)
bat1.finalizing()
ball1.finalizing()
win.mainloop()