# Documentation

# Description #
A red ball bouncing from the wall, which you should hit with a paddle. If you miss it - something bad happens.
''Play'' the code find found out what.

# Live demo #

https://github.com/sldimitrov/Projects/assets/135168991/8883bdde-f355-4053-a36a-10d641163c97

# Technology stack #
Python was involved, of course.
I had also used several libraries.
Tkinter, random and time.

# Screenshots #
Here you can see the full start-screen. 
The game is waiting for the user to press Enter.

![Screenshot 2023-12-20 223850](https://github.com/sldimitrov/Projects/assets/135168991/14fb78f2-4cdf-4720-81d8-f167ddc596b2)

# Adjustments #
Hello viewer! I am so glad that you are reading this. I hope you like my project and if I am right dont forget to Star-up the repository!

In this header I am going to show you some things you can change in the code to make the game look alike it's your own.

* Change the text on the down-right angle.
First go to ... line and... 

```python 
from tkinter import *
import random
import time

counter = 0


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.x += self.paddle.x
                self.score.hit()
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if pos[3] >= self.canvas_height:
            self.y = -3
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3


class Paddle:
    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

    def start_game(self, evt):
        self.started = True

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.started = False
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<space>', self.start_game)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2


class Score:
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(470, 10, text=self.score, fill=color,
                                     font=('Courier', 22))

    def hit(self):
        self.score += 10
        self.canvas.itemconfig(self.id, text=self.score)


tk = Tk()
tk.title('The BOuNCiNG Ball')
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

score = Score(canvas, 'purple')
paddle = Paddle(canvas, 'gold')
ball = Ball(canvas, paddle, 'red')
game_over_text = canvas.create_text(250, 200, text='FUN'S OVER',
                                    state='hidden', font=('Times', 20))
points = canvas.create_text(430, 370, text='made by SL', font=(('Agbalumo', 15)))

while 1:
    if ball.hit_bottom == False and paddle.started == True:
        ball.draw()
        paddle.draw()
    if ball.hit_bottom == True:
        canvas.itemconfig(game_over_text, state='normal')
        time.sleep(0.08)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    if counter == 0:
        time.sleep(3)

    counter += 1
```

