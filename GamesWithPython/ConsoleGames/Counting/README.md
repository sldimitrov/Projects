# Documentation

# Description #
Guess a number between 1 and 100!
The game is something like playing on warm and cold. Each time you enter your guess the program tells you wether you should go up or down. My personal best is winning it with just two moves. It's your turn to beat me now!🔢
# Live demo #

https://github.com/sldimitrov/Projects/assets/135168991/a6b36eb5-67dc-4cc6-8525-bda6f1430d38

# Knowledge stack #
The interesting module we are using here is (random), he is build-in so you don't need to install it. We are using it to choose a random number in the given range and it guarantees us that the number we are searching for is going to be different every single time. For the operation we are using just the following two lines which are the beggining of our program.
 ```
import random
special = random.randint(1, 100)
 ```
Other stuff we are using are if-else-statements within a while loop. A little of text formatting at the end and that's all ;)

# Adjustments #
If you want to make the program more advanced - you first need to fork the repository. That will allows you to play with the code!
Let's say that inster of choosing between 100 numbers you want to do it between 1000. The only thing you will change is the number in the 3th line of the code.
 ```
import random
special = random.randint(1, 1000)
 ```
