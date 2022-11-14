import turtle
import numpy as np

# def visualizer_solution():


class visualization:
    def __init__(self, length, width, gridwidth):
        self.length = length
        self.width = width
        self.gridwidth = gridwidth
        self.startx = int(gridwidth * width / 2)
        self.starty = int(gridwidth * length / 2)
        
    def visualize_grid(self):
        """
        Visualize the grid using turtle graphics
        :param length: length of the grid
        :param width: width of the grid

        :return: None
        """
        turtle.ht()
        # Set up the window and its attributes
        turtle.setup(500, 700)
        turtle.bgcolor("Dimgrey")
        # turtle.bgpic("background.png")
        turtle.title("Lazors CRACKED！")
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
            turtle.fillcolor("aliceblue")
        if type == "B":
            turtle.fillcolor("lightsteelblue")
        if type == "C":
            turtle.fillcolor("slategray")
            
        for z in range(4):
            turtle.fd(gridwidth)
            turtle.left(90)
        turtle.end_fill()

    def visualize_lazor(self, lazor_ori, lazor_dir):
        """
        Visualize the lazor using turtle graphics
        :param lazor: lazor object
        :param gridwidth: width of the grid

        :return: None
        """     
        gridwidth = self.gridwidth/2
        
        # Draw the lazor origin
        x = lazor_ori[0] * gridwidth - self.startx
        y = - lazor_ori[1] * gridwidth + self.starty
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color("white")
        turtle.dot()
        
        # Draw the lazor direction
        if lazor_dir == [1,1]:
            angle = 45
        if lazor_dir == [-1, 1]:
            angle = 135
        if lazor_dir == [-1, -1]:
            angle = 225
        if lazor_dir == [1, -1]:
            angle = 315
        turtle.seth(angle)
        turtle.color("red")
        turtle.pensize(6)
        turtle.forward(1000)
 

if __name__ == '__main__':

    # Set the parameters for the grid
    solution = visualization(5, 3, 80)
    
    # Visualize the grid
    solution.visualize_grid()
    # Visualize the blocks
 
    solution.visualize_blocks("A", [0,1])
    solution.visualize_blocks("A", [2,2])
    solution.visualize_blocks("A", [0,3])
    solution.visualize_blocks("A", [2,4])

    # Visualize the lazor
    solution.visualize_lazor([4,1], [-1,-1])
    
    turtle.mainloop()