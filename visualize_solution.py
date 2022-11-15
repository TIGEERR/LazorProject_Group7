'''
This is the file of the Visualizer, which is used to visualize the solution in GUI.

Author: Anruo Shen, Taichi Liu

'''


import turtle
import numpy as np

class visualize_solution():
    '''
    This is the main function of the Visualizer,
    which is used to visualize the solution in GUI.
    '''
    def __init__(self, block_grid, gridwidth, blocks, lazors):
        self.length = np.shape(block_grid)[0]
        self.width = np.shape(block_grid)[1]
        self.gridwidth = gridwidth
        self.startx = int(gridwidth * self.width / 2)
        self.starty = int(gridwidth * self.length / 2)
        self.blocks = blocks
        self.lazors = lazors
        self.myturtle = turtle.Turtle()

    def visualize_grid(self):
        '''
        This function is used to draw the grid of the puzzle
        '''
        myturtle = self.myturtle
        wn = turtle.Screen()
        myturtle.ht()
        # Set up the window and its attributes
        wn.setup(500, 700)
        wn.bgcolor("Dimgrey")
        # myturtle.bgpic("background.png")
        wn.title("Lazors CRACKED!")
        myturtle.speed(0)

        # Set the parameters for the grid
        a = self.width
        b = self.length
        gridwidth = self.gridwidth
        startx = int(gridwidth * a / 2)
        starty = int(gridwidth * b / 2)
        block_width = gridwidth

        # Draw the horizontal lines
        x = -startx
        for y in range(-starty, starty + 1, block_width):
            myturtle.color("dimgrey")
            myturtle.pensize(10)
            myturtle.penup()
            myturtle.goto(x,y)
            myturtle.pendown()
            myturtle.fd(block_width * a)

        # Draw the vertical lines
        y = starty
        myturtle.right(90)
        for x in range(-startx, startx + 1, block_width):
            myturtle.pensize(10)
            myturtle.penup()
            myturtle.goto(x,y)
            myturtle.pendown()
            myturtle.fd(block_width * b)

        # Color the grid
        for x in range(-startx, startx, block_width):
            for y in range(-starty, starty, block_width):
                myturtle.penup()
                myturtle.goto(x,y)
                myturtle.pendown()
                myturtle.begin_fill()
                myturtle.fillcolor("darkgrey")
                for z in range(4):
                    myturtle.left(90)
                    myturtle.fd(block_width)
                myturtle.end_fill()


    def visualize_points(self, end_points, lazor_origin):
        """
        Visualize the start points and end points of lazor
        using turtle graphics
        """
        myturtle = self.myturtle
        for point in end_points:
            x = point[0] * self.gridwidth/2 - self.startx
            y = - point[1] * self.gridwidth/2 + self.starty
            myturtle.penup()
            myturtle.goto(x, y)
            myturtle.pendown()
            myturtle.color("mediumslateblue")
            myturtle.dot()

        # Draw the lazor origin
        myturtle.pensize(10)
        for i in range(len(lazor_origin)):
            x = lazor_origin[i]["x"] * self.gridwidth/2 - self.startx
            y = - lazor_origin[i]["y"] * self.gridwidth/2 + self.starty
            myturtle.penup()
            myturtle.goto(x, y)
            myturtle.pendown()
            myturtle.color("red")
            myturtle.dot()


    def visualize_blocks(self, type, position):
        """
        Visualize the blocks using myturtle graphics
        """
        myturtle = self.myturtle
        gridwidth = self.gridwidth

        myturtle.penup()
        myturtle.goto(position[0] * gridwidth - self.startx,\
            - position[1] * gridwidth + self.starty)
        myturtle.pendown()
        myturtle.begin_fill()
        if type == "A":
            myturtle.fillcolor("slategray")
        if type == "B":
            myturtle.fillcolor("black")
        if type == "C":
            myturtle.fillcolor("aliceblue")
        if type == "o":
            myturtle.fillcolor("darkgrey")
        if type == "x":
            myturtle.fillcolor("DimGrey")
        for z in range(4):
            myturtle.fd(gridwidth)
            myturtle.left(90)
        myturtle.end_fill()

    def visualize_lazor(self, lazor_path):
        """
        Visualize the lazor using turtle graphics
        :param lazor: lazor object
        :param gridwidth: width of the grid

        :return: None
        """
        myturtle = self.myturtle
        gridwidth = self.gridwidth/2

        for i in range (len(lazor_path)):
            x = lazor_path[i][0][0] * self.gridwidth/2 - self.startx
            y = - lazor_path[i][0][1] * self.gridwidth/2 + self.starty
            myturtle.penup()
            myturtle.goto(x, y)
            myturtle.pendown()
            for j in range (len(lazor_path[i])):
                if j == len(lazor_path[i]) - 1:
                    break
                lazor_dir = [lazor_path[i][j+1][0] - lazor_path[i][j][0], \
                    lazor_path[i][j+1][1] - lazor_path[i][j][1]]
                distance = np.sqrt(2) * gridwidth
                if j == len(lazor_path[i]) - 2:
                    distance = 1000
                # Draw the lazor direction
                if lazor_dir == [1,1]:
                    angle = 315
                if lazor_dir == [-1, 1]:
                    angle = 225
                if lazor_dir == [-1, -1]:
                    angle = 135
                if lazor_dir == [1, -1]:
                    angle = 45
                myturtle.seth(angle)
                myturtle.color("red")
                myturtle.pensize(6)
                myturtle.forward(distance)

def visualizer(block_grid, gridwidth, blocks, lazors, end_points, lazor_origin):
    '''
    This is the main function of the Visualizer
    '''
    # Set the parameters for the grid
    solution = visualize_solution(block_grid, gridwidth, blocks, lazors)

    # Visualize the grid
    solution.visualize_grid()

    # Visualize the blocks
    for i in range (len(blocks)):
        solution.visualize_blocks(blocks[i][0], blocks[i][1])

    solution.visualize_points(end_points, lazor_origin)
    # Visualize the lazor
    solution.visualize_lazor(lazors)

    turtle.mainloop()
    