# Documentation

# Description #
This calculator has all of the most commonly-used math operations ➗ It looks basic itself on the first look but it's a program that could help you understand why writing code in a function is helpful and why we should use them ➕ They are the tool that allow us to write some functionallity once but use it countless times ✖️ This thing saves us money and time, of course, which is our most-valuable resource ✔️ Without further delay let me introduce you ➖ My calculator!(´｡• ◡ •｡`) ♡

# Live demo #

https://github.com/sldimitrov/Projects/assets/135168991/21810247-eb6b-4746-ac1c-873f338ad899

# Knowledge stack #
Python was involved, of course.
To exercise with functions were the main scope of the script. There are also some text-processing operations in it, if-else-statements, Loops and that's all.

# Screenshots #
* The menu() functions, that only prints the menu below.
Once you terminate the program the same menu function is called and you can see the first messages that appears in the console. The program is waiting for the user to choose between 6 options.
![Screenshot 2023-12-22 003750](https://github.com/sldimitrov/Projects/assets/135168991/6045bbeb-4a0b-472d-a247-b0f3cfffb2a5)


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
# In fact, you can change whatever you want! These were just few examples of how the game could be modified. Thank you for the attention, see you in the next project! ;)#
