'''
This is the file of the Visualizer, which is used to visualize the solution in GUI.

Author: Anruo Shen, Taichi Liu

'''


import turtle
import numpy as np

class visualize_solution():
    def __init__(self, block_grid, gridwidth, blocks, lazors):
        self.length = np.shape(block_grid)[0]
        self.width = np.shape(block_grid)[1]
        self.gridwidth = gridwidth
        self.startx = int(gridwidth * self.width / 2)
        self.starty = int(gridwidth * self.length / 2)
        self.blocks = blocks
        self.lazors = lazors
        
    def visualize_grid(self):
        turtle.ht()
        # Set up the window and its attributes
        turtle.setup(500, 700)
        turtle.bgcolor("Dimgrey")
        # turtle.bgpic("background.png")
        turtle.title("Lazors CRACKED!")
        turtle.speed(0)
        
        # Set the parameters for the grid
        a = self.width
        b = self.length
        gridwidth = self.gridwidth
        startx = int(gridwidth * a / 2)
        starty = int(gridwidth * b / 2)
        block_width = gridwidth
        
        # Draw the horizontal lines
        x = -startx
        block_width
        for y in range(-starty, starty + 1, block_width):
            turtle.color("dimgrey")
            turtle.pensize(10)
            turtle.penup()
            turtle.goto(x,y)
            turtle.pendown()
            turtle.fd(block_width * a)
            
        # Draw the vertical lines  
        y = starty
        turtle.right(90)
        for x in range(-startx, startx + 1, block_width):
            turtle.pensize(10)
            turtle.penup()
            turtle.goto(x,y)
            turtle.pendown()
            turtle.fd(block_width * b)  
        
        # Color the grid
        for x in range(-startx, startx, block_width):
            for y in range(-starty, starty, block_width):
                turtle.penup()
                turtle.goto(x,y)
                turtle.pendown()
                turtle.begin_fill()
                turtle.fillcolor("darkgrey")
                for z in range(4):
                    turtle.left(90)
                    turtle.fd(block_width)
                turtle.end_fill()
                
                
    def visualize_points(self, end_points, lazor_origin):
        """
        Visualize the end points using turtle graphics
        :param end_points: end points of the lazors

        :return: None
        """
        for point in end_points:
            x = point[0] * self.gridwidth/2 - self.startx
            y = - point[1] * self.gridwidth/2 + self.starty
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            turtle.color("mediumslateblue")
            turtle.dot()
        
        # Draw the lazor origin
        turtle.pensize(10)
        for i in range(len(lazor_origin)):
            x = lazor_origin[i]["x"] * self.gridwidth/2 - self.startx
            y = - lazor_origin[i]["y"] * self.gridwidth/2 + self.starty
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            turtle.color("red")
            turtle.dot()
        
      
    def visualize_blocks(self, type, position):
        """
        Visualize the blocks using turtle graphics
        :param position: position of the blocks

        :return: None
        """
        gridwidth = self.gridwidth
        
        turtle.penup()
        turtle.goto(position[0] * gridwidth - self.startx, - position[1] * gridwidth + self.starty)
        turtle.pendown()
        turtle.begin_fill()
        if type == "A":
            turtle.fillcolor("slategray")
        if type == "B":
            turtle.fillcolor("black")
        if type == "C":
            turtle.fillcolor("aliceblue")
        if type == "o":
            turtle.fillcolor("darkgrey")
        if type == "x":
            turtle.fillcolor("DimGrey")
        for z in range(4):
            turtle.fd(gridwidth)
            turtle.left(90)
        turtle.end_fill()

    def visualize_lazor(self, lazor_path):
        """
        Visualize the lazor using turtle graphics
        :param lazor: lazor object
        :param gridwidth: width of the grid

        :return: None
        """     
        gridwidth = self.gridwidth/2
        
        for i in range (len(lazor_path)):
            x = lazor_path[i][0][0] * self.gridwidth/2 - self.startx
            y = - lazor_path[i][0][1] * self.gridwidth/2 + self.starty
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            for j in range (len(lazor_path[i])):
                if j == len(lazor_path[i]) - 1:
                    break
                lazor_dir = [lazor_path[i][j+1][0] - lazor_path[i][j][0], lazor_path[i][j+1][1] - lazor_path[i][j][1]]
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
                turtle.seth(angle)
                turtle.color("red")
                turtle.pensize(6)
                turtle.forward(distance)
 
def visualizer(block_grid, gridwidth, blocks, lazors, end_points, lazor_origin):
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
    