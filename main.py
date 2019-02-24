from tkinter import *

import random

height = 500
width = 800

image_name = "DVD_image.gif"
image_width = 50
image_height = 26

x_y_ratio = random.uniform(0.25, 0.75)
print(x_y_ratio)

velocity = 200   # px/s
fps = 60

if random.randint(0, 1) == 1:
    x_speed = velocity * x_y_ratio
    y_speed = velocity * (1 - x_y_ratio)
else:
    x_speed = - velocity * x_y_ratio
    y_speed = - velocity * (1 - x_y_ratio)


class Canvas_(Canvas):
    def __init__(self):
        Canvas.__init__(self, root, bg="#cccccc")
        self.parent = root

        self.image_file = PhotoImage(file=image_name)

        self.x_speed = x_speed
        self.y_speed = y_speed

        self.x = 300
        self.y = 300

        self.image = self.create_rectangle(self.x, self.y, self.x + 10, self.y + 10, fill="#ff0000")
        self.update()

    def update(self):
        self.delete(self.image)
        self.x = self.x + self.x_speed/fps
        self.y = self.y + self.y_speed/fps
        self.image = self.create_image(self.x, self.y, image=self.image_file, anchor=NW)

        if self.x <= 0 or self.x + image_width >= width:
            self.x_speed = - self.x_speed
        elif self.y <= 0 or self.y + image_height >= height:
            self.y_speed = - self.y_speed

        self.after(round(1000 / fps), self.update)


root = Tk()
root.geometry(str(width)+"x"+str(height))
root.title("DVD bounce")

canvas = Canvas_()
print(canvas)
canvas.place(x=0, y=0, width=width, height=height)

root.mainloop()
