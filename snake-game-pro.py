import tkinter
from tkinter import *

from random import randint, choice

import os
import sys
from PIL import Image, ImageTk




class Snake:
    def __init__(self, window):
        self.window = window
        self.canvas = canvas
        self.BODY_SIZE = 3
        self.coordinates = []
        self.squares = []
        self.SLOWNESS = 200
        self.SNAKE_COLOR = "green"
        self.BACKGROUND_COLOR = 'black'
        self.score = 0
        self.direction = "Right"
        self.GAME_WIDTH = 800
        self.GAME_HEIGHT = 800
        self.SPACE_SIZE = 40
        self.window.title("Snake Game")
        self.canvas = canvas
        self.window.resizable(False, False)
        self.label = Label(self.window, text=f"Score1: {self.score}", font=("Courier", 20))
        self.label.pack()
        self.back = Image.open("33.png")
        self.back = self.back.resize((800, 800))
        self.back_photo = ImageTk.PhotoImage(self.back)
        self.canvas.create_image(0, 0, anchor="nw", image=self.back_photo)

        self.restart = Button(self.window, text="Restart", fg="red", command=self.restart_program)
        self.restart.pack()
        for i in range(3):
            self.coordinates.append([320, 320])

        for x, y in self.coordinates:
            self.square = self.canvas.create_rectangle(x, y, x + 40, y + 40, tag="snake", fill="green")
            self.squares.append(self.square)

        self.window.update()
        self.food = self.Food(self.GAME_WIDTH, self.GAME_HEIGHT, self.SPACE_SIZE, self.canvas)
        self.mushroom = self.Mushroom(self.GAME_WIDTH, self.GAME_HEIGHT, self.SPACE_SIZE, self.canvas)

        self.next_turn()
        self.window.bind("<KeyPress>", lambda event: self.key_pressed(event))
        self.check_game_over()
        self.window.update()


    def restart_program(self):
        self.path = sys.executable
        os.execl(self.path, self.path, *sys.argv)

    def check_game_over(self):
        x, y = self.coordinates[0]
        if x < 0 or x > 800:
            return True
        if y < 0 or y > 800:
            return True

        for sq in self.coordinates[1:]:
            if x == sq[0] and y == sq[1]:
                return True
        return False

    def game_over(self):
        self.canvas.delete(ALL)
        self.canvas.create_text(self.canvas.winfo_width() // 2, self.canvas.winfo_height() // 2,
                                font=("Arial", 20, "bold"),
                                text="GAME OVER", fill="red", tags="gameover")

    def next_turn(self):
        x, y = self.coordinates[0]
        if self.direction == "Up":
            y -= self.SPACE_SIZE
        elif self.direction == "Down":
            y += self.SPACE_SIZE
        elif self.direction == "Left":
            x -= self.SPACE_SIZE
        elif self.direction == "Right":
            x += self.SPACE_SIZE
        self.coordinates.insert(0, [x, y])
        self.square = self.canvas.create_rectangle(x, y, x + self.SPACE_SIZE, y + self.SPACE_SIZE,
                                                   fill=self.SNAKE_COLOR, tags="snake")
        self.squares.insert(0, self.square)
        if x == self.food.coordinates[1] and y == self.food.coordinates[0]:
            self.score += 1
            self.label.config(text=f"Score1: {self.score}")
            self.canvas.delete("food")
            self.food = Snake.Food(self.GAME_WIDTH, self.GAME_HEIGHT, self.SPACE_SIZE, self.canvas)
            if self.score % 8 == 0:
                self.mushroom = self.Mushroom(self.GAME_WIDTH, self.GAME_HEIGHT, self.SPACE_SIZE, self.canvas)
            if self.SLOWNESS == 45:
                self.SLOWNESS = 70
                self.SNAKE_COLOR = "green"
            else:
                self.SLOWNESS -= 5
        elif x == self.mushroom.coordinates[1] and y == self.mushroom.coordinates[0]:
            colors = ["red", "blue", "gray", "yellow", "orange", "black"]
            self.SNAKE_COLOR = choice(colors)
            self.SLOWNESS = 60
            self.canvas.delete("mushroom")
        else:
            del self.coordinates[-1]
            self.canvas.delete(self.squares[-1])
            del self.squares[-1]
        if self.check_game_over():
            self.game_over()
        else:
            self.window.after(self.SLOWNESS, self.next_turn)

    def key_pressed(self, event):
        if event.keysym == 'Up':
                self.direction = 'Up'
        elif event.keysym == 'Down':
                self.direction = 'Down'
        elif event.keysym == 'Left':
                self.direction = 'Left'
        elif event.keysym == 'Right':
                self.direction = 'Right'



    class Food:
        def __init__(self, GAME_WIDTH, GAME_HEIGHT, SPACE_SIZE, canvas):
            self.GAME_WIDTH = GAME_WIDTH
            self.GAME_HEIGHT = GAME_HEIGHT
            self.SPACE_SIZE = SPACE_SIZE
            self.apple = Image.open("4.png")
            self.apple = self.apple.resize((44, 42))
            self.apple_photo = ImageTk.PhotoImage(self.apple)
            x = randint(0, ((self.GAME_WIDTH // self.SPACE_SIZE) - 1)) * self.SPACE_SIZE
            y = randint(0, ((self.GAME_WIDTH // self.SPACE_SIZE) - 1)) * self.SPACE_SIZE
            self.coordinates = [x, y]
            canvas.create_image(y, x, anchor=tkinter.NW, image=self.apple_photo, tag="food")

    class Mushroom:
        def __init__(self, GAME_WIDTH, GAME_HEIGHT, SPACE_SIZE, canvas):
            self.GAME_WIDTH = GAME_WIDTH
            self.GAME_HEIGHT = GAME_HEIGHT
            self.SPACE_SIZE = SPACE_SIZE
            self.apple = Image.open("15.png")
            self.apple = self.apple.resize((64, 62))
            self.apple_photo = ImageTk.PhotoImage(self.apple)
            x = randint(0, ((self.GAME_WIDTH // self.SPACE_SIZE) - 1)) * self.SPACE_SIZE
            y = randint(0, ((self.GAME_WIDTH // self.SPACE_SIZE) - 1)) * self.SPACE_SIZE
            self.coordinates = [x, y]
            canvas.create_image(y, x, anchor=tkinter.NW, image=self.apple_photo, tag="mushroom")


class SnakeGame2:
    def __init__(self, window1):
        self.window = window1
        self.coordinates = []
        self.coordinates2 = []
        self.squares = []
        self.squares2 = []
        self.direction = "down"
        self.direction2 = "w"
        self.GAME_WIDTH = 800
        self.GAME_HEIGHT = 800
        self.SPACE_SIZE = 40
        self.SLOWNESS = 200
        self.SLOWNESS2 = 200
        self.SNAKE_COLOR = "green"
        self.SNAKE_COLOR2 = "red"
        self.BACKGROUND_COLOR = "black"
        self.FOOD_COLOR = "yellow"
        self.health1 = 3
        self.health2 = 3
        self.health3 = 0
        self.score = 0
        self.score2 = 0
        self.win = "Green"
        self.window.title("Snake Game")
        self.canvas = canvas
        self.window.bind("<KeyPress>", self.key_pressed)
        self.snake1 = self.Snake(self.canvas)
        self.snake2 = self.Snake2(self.canvas)
        self.label = Label(self.window, text=f"Score1: {self.score}", font=("Courier", 20))
        self.label.pack()
        self.label2 = Label(self.window, text=f"Score2: {self.score2}", font=("Courier", 20))
        self.label2.pack()
        self.label3 = Label(self.window, text=f"Green: {self.health1}❤️ ", fg="green", font=10, background="black")
        self.label3.place(x=45, y=45)
        self.label4 = Label(self.window, text=f"Red: {self.health2}❤️ ", fg="red", font=20, background="black")
        self.label4.place(x=600, y=45)
        self.back = Image.open("321.png")
        self.back = self.back.resize((800, 800))
        self.back_photo = ImageTk.PhotoImage(self.back)
        self.canvas.create_image(0, 0, anchor="nw", image=self.back_photo)
        self.restart = Button(self.window, text="Restart", fg="red", command=self.restart_program)
        self.restart.pack()
        self.food = self.Food(self.GAME_WIDTH, self.GAME_HEIGHT, self.SPACE_SIZE, self.canvas)
        self.health = self.Health(self.GAME_WIDTH, self.GAME_HEIGHT, self.SPACE_SIZE, self.canvas)
        self.next_turn(self.snake1, self.snake2)
        self.check_game_over()
        self.check_game_over2()
        self.window.update()

    def next_turn(self, snake1, snake2):
        x, y = snake1.coordinates[0]
        if self.direction == "Up":
            y -= self.SPACE_SIZE
        elif self.direction == "Down":
            y += self.SPACE_SIZE
        elif self.direction == "Left":
            x -= self.SPACE_SIZE
        elif self.direction == "Right":
            x += self.SPACE_SIZE

        snake1.coordinates.insert(0, [x, y])
        square = self.canvas.create_rectangle(x, y, x + self.SPACE_SIZE, y + self.SPACE_SIZE, fill=self.SNAKE_COLOR, tags="snake1")
        snake1.squares.insert(0, square)

        a, b = snake2.coordinates2[0]
        if self.direction2 == "Up":
            b -= self.SPACE_SIZE
        elif self.direction2 == "Down":
            b += self.SPACE_SIZE
        elif self.direction2 == "Left":
            a -= self.SPACE_SIZE
        elif self.direction2 == "Right":
            a += self.SPACE_SIZE

        snake2.coordinates2.insert(0, [a, b])
        square = self.canvas.create_rectangle(a, b, a + self.SPACE_SIZE, b + self.SPACE_SIZE, fill=self.SNAKE_COLOR2, tags="snake2")
        snake2.squares2.insert(0, square)

        if x == self.food.coordinates[1] and y == self.food.coordinates[0]:
            self.health3 += 1
            self.score += 1
            self.label.config(text=f"Score1: {self.score}")
            self.canvas.delete("food")
            self.food = self.Food(self.GAME_WIDTH, self.GAME_HEIGHT, self.SPACE_SIZE, self.canvas)
        else:
            del snake1.coordinates[-1]
            self.canvas.delete(snake1.squares[-1])
            del snake1.squares[-1]

        if a == self.food.coordinates[1] and b == self.food.coordinates[0]:
            self.score2 += 1
            self.health3 += 1
            self.label2.config(text=f"Score2: {self.score2}")
            self.canvas.delete("food")
            self.food = self.Food(self.GAME_WIDTH, self.GAME_HEIGHT, self.SPACE_SIZE, self.canvas)
        else:
            del snake2.coordinates2[-1]
            self.canvas.delete(snake2.squares2[-1])
            del snake2.squares2[-1]

        if self.health3 > 5:
            self.health = self.Health(self.GAME_WIDTH, self.GAME_HEIGHT, self.SPACE_SIZE, self.canvas)
            self.health3 = 0
        if x == self.health.coordinates[1] and y == self.health.coordinates[0]:
            self.health1 += 1
            self.label3.config(text=f"Green: {self.health1}")
            self.canvas.delete("health")
        if a == self.health.coordinates[1] and b == self.health.coordinates[0]:

            self.health2 += 1
            self.label4.config(text=f"Red: {self.health2}")
            self.canvas.delete("health")

        if self.check_game_over():
            self.game_over()
        elif self.check_game_over2():
            self.game_over()
        else:
            self.window.after(self.SLOWNESS, self.next_turn, snake1, snake2)

    def key_pressed(self, event):
        if event.keysym == 'Up':
            self.direction = 'Up'
        elif event.keysym == 'Down':
            self.direction = 'Down'
        elif event.keysym == 'Left':
            self.direction = 'Left'
        elif event.keysym == 'Right':
            self.direction = 'Right'

        if event.char == 'w':
            self.direction2 = 'Up'
        elif event.char == 's':
            self.direction2 = 'Down'
        elif event.char == 'a':
            self.direction2 = 'Left'
        elif event.char == 'd':
            self.direction2 = 'Right'

    def check_game_over(self):
        self.label3.config(text=f"Green: {self.health1}❤️ ")
        self.head = self.snake2.coordinates2[0]
        x, y = self.snake1.coordinates[0]
        if self.health1 == 0:
            self.win = "Red"
            return True
        if x < -5 or x > self.GAME_WIDTH + 5:
            self.health1 -= 1
        if y < -5 or y > self.GAME_HEIGHT + 5:
            self.health1 -= 1
        for sq in self.snake2.coordinates2[1:]:
            if x == sq[0] and y == sq[1]:
                self.health1 -= 1
        for segment in self.snake1.coordinates[1:]:
            if self.head == segment:
                self.health1 -= 1

        return False

    def check_game_over2(self):
        self.label4.config(text=f"Green: {self.health2}❤️ ")
        a, b = self.snake2.coordinates2[0]
        self.head = self.snake1.coordinates[0]
        if self.health2 == 0:
            return True
        if a < -5 or a > self.GAME_WIDTH + 5:
            self.health2 -= 1
        if b < -5 or b > self.GAME_WIDTH + 5:
            self.health2 -= 1

        for sq in self.snake1.coordinates[1:]:
            if a == sq[0] and b == sq[1]:
                self.health2 -= 1
        for segment in self.snake2.coordinates2[1:]:
            if self.head == segment:
                self.health2 -= 1

        return False

    def game_over(self):
        self.canvas.delete(ALL)
        self.canvas.create_text(self.canvas.winfo_width() // 2, self.canvas.winfo_height() // 2, font=("Arial", 20, "bold"),
                           text=f"GAME OVER\nThe winner:*{self.win}*", fill="red", tags="gameover")

    def restart_program(self):
        path = sys.executable
        os.execl(path, path, *sys.argv)


    class Food:
        def __init__(self, GAME_WIDTH, GAME_HEIGHT, SPACE_SIZE, canvas):
            self.GAME_WIDTH = GAME_WIDTH
            self.GAME_HEIGHT = GAME_HEIGHT
            self.SPACE_SIZE = SPACE_SIZE
            self.apple = Image.open("4.png")
            self.apple = self.apple.resize((44, 42))
            self.apple_photo = ImageTk.PhotoImage(self.apple)
            x = randint(0, ((self.GAME_WIDTH // self.SPACE_SIZE) - 1)) * self.SPACE_SIZE
            y = randint(0, ((self.GAME_WIDTH // self.SPACE_SIZE) - 1)) * self.SPACE_SIZE
            self.coordinates = [x, y]
            canvas.create_image(y, x, anchor=tkinter.NW, image=self.apple_photo, tag="food")

    class Health:
        def __init__(self, GAME_WIDTH, GAME_HEIGHT, SPACE_SIZE, canvas):
            self.GAME_WIDTH = GAME_WIDTH
            self.GAME_HEIGHT = GAME_HEIGHT
            self.SPACE_SIZE = SPACE_SIZE
            self.health = Image.open("5.png")
            self.health = self.health.resize((46, 48))
            self.health_photo = ImageTk.PhotoImage(self.health)
            x = randint(0, ((GAME_WIDTH // SPACE_SIZE) - 1)) * SPACE_SIZE
            y = randint(0, ((GAME_WIDTH // SPACE_SIZE) - 1)) * SPACE_SIZE
            self.coordinates = [x, y]
            canvas.create_image(y, x, anchor=tkinter.NW, image=self.health_photo, tag="health")

    class Snake:
        def __init__(self, canvas):
            self.bodysize = 3
            self.coordinates = []
            self.squares = []
            self.canvas = canvas
            for i in range(3):
                self.coordinates.append([320, 320])

            for x, y in self.coordinates:
                square = self.canvas.create_rectangle(x, y, x + 40, y + 40, fill="green", tag="snake1")
                self.squares.append(square)

    class Snake2:
        def __init__(self, canvas):
            self.bodysize2 = 3
            self.coordinates2 = []
            self.squares2 = []
            self.canvas = canvas

            for i in range(3):
                self.coordinates2.append([520, 520])

            for a, b in self.coordinates2:
                square = self.canvas.create_rectangle(a, b, a + 40, b + 40, fill="red", tag="snake2")
                self.squares2.append(square)









root = Tk()
def start_single_player():
    label.destroy()
    canvas.delete("snake_")

    single_player_button.destroy()
    multi_player_button.destroy()
    Snake(root)



def start_multi_player():
    label.destroy()
    canvas.delete("snake_")
    single_player_button.destroy()
    multi_player_button.destroy()
    SnakeGame2(root)




root.title("Snake Game pro")
canvas = Canvas(root, bg='black', height=800, width=800)
snake_ = Image.open("44.png")
snake_ = snake_.resize((278, 278))
snake_photo = ImageTk.PhotoImage(snake_)
canvas.create_image(270, 450, anchor=tkinter.NW, image=snake_photo, tag="snake_")
canvas.pack()

label = Label(root, text="Dont try mushroom🍄🍄🍄🍄\nFor tow player second snake move with w,a,s,d", font=("Arial", 16), bg="black", fg="green")
label.place(x=190, y=120)


single_player_button = Button(root, text="*start-single-player*", font=("Arial", 13),  command=start_single_player, width=20, fg="green", bg="black")
single_player_button.place(x=300, y=200)


multi_player_button = Button(root, text="**start-two-player**", font=("Arial", 13), command=start_multi_player, width=20, fg="red", bg="black")
multi_player_button.place(x=300, y=250)


root.mainloop()
