# Documentation

# Description #
When starting as Red Ball, you are a ball, stuck in a world of wonders.
A ball bouncing from the wall, which you should hit with a paddle. If you miss it - something bad happens.
''Play'' the code find found out what.

# Live demo #

https://github.com/sldimitrov/Projects/assets/135168991/8883bdde-f355-4053-a36a-10d641163c97

# Technology stack #
Python was involved, of course.
I had also used several libraries.
Tkinter, random and time.

# Screenshots #
Here you can see the full start-screen. 
The game is waiting for the user to press Space.

![Screenshot 2023-12-20 223850](https://github.com/sldimitrov/Projects/assets/135168991/14fb78f2-4cdf-4720-81d8-f167ddc596b2)

# Adjustments #
Hello viewer! I am so glad that you are reading this. I hope you like my project and if I'm right don't forget to *star or fork the repository*!

In this header I am going to show you some things you can change in the code to make the game look alike it's your own.

* Change the text on the down-right angle.
First go to **line 111** of the code and replace - "text = 'made by SL'" with 'made by Leonardo Da Vinci', for example

```python 
points = canvas.create_text(430, 370, text='made by SL', font=(('Agbalumo', 15)))
```
* To change the color of the ball you should go to line 108
```python 
ball = Ball(canvas, paddle, 'red')
```

* And for the color of the paddle - line 107
```python 
paddle = Paddle(canvas, 'gold')
```
## In fact, you can change whatever you want! These were just few examples of how the game could be modified. Thank you for the attention, see you in the next project! ;)
