'''
This file read in the game setting from .bff file and store
them in python data structures.

Author: Anruo Shen

'''

def read_setting(f):
    '''
    This function will read in the lazor game setting
    
    Input: file (.bff)
    Output: block_grid, blocks, lazor, endpoint
    '''
    file = open(f, 'r')
    
    # initialize the data structure
    blocks = {'A':0, 'B':0, 'C':0}
    lazors = []
    end_points = []

    for line in file:
        if line[0] == 'G':
            block_grid = read_grid(file)
        elif line[0] == 'A' or line[0] == 'B' or line[0] =='C':
             blocks = read_blocks(line, blocks)
        elif line[0] == 'L':
            lazors.append(read_lazor(line))
        elif line[0] == 'P':
            point = read_endpoint(line)
            end_points.append(point)
        
    return block_grid, blocks, lazors, end_points


def read_grid(file):
    '''
    This function parse the grid information from the file
    
    Input: file (.bff)
    Output: block grid (array)
    '''
    # read the grid size
    copy = []
    height = 0
    for line in file:
        if line == "GRID STOP\n":
            break
        # locate the grid information
        height += 1
        line = line.strip().replace(' ', '')
        copy.append(line)
        if height == 1:
            width = len(line)
    # create the grid
    block_grid = [[0 for x in range(width)] for y in range(height)]
    
    # read the grid information(0 - block allowed, 1 - no block allowed)
    for row in range(height):
        for col in range(width):
            if copy[row][col] == 'o':
                block_grid[row][col] = 0
            else:
                block_grid[row][col] = 1
    
    return block_grid


def read_blocks(line, blocks):
    '''
    This function parse the blocks information from the file
    
    Input: file (.bff)
    Output: blocks (array)
    '''
    for idx, letter in enumerate(blocks):
        if letter == line[0]:
            blocks[letter] = int(line[2])
    return blocks


def read_lazor(line):
    '''
    This function parse the lazor information from the file
    
    Input: file (.bff)
    Output: lazor (array)
    '''
    # read the lazor information
    line = line.strip().split(' ')
    return ({'x': int(line[1]), 'y': int(line[2]), 'vx': int(line[3]), 'vy': int(line[4])})


def read_endpoint(line):
    '''
    This function parse the endpoint information from the file
   
    Input: file (.bff)
    Output: endpoint (array)
    '''
    # read the endpoint information
    line = line.strip().split(' ')
    point = (int(line[1]), int(line[2]))
    
    return point


if __name__ == "__main__":
    f = './LazorTemplates/mad_7.bff'
    block_grid, blocks, lazors, end_points = read_setting(f)
    
    print(block_grid, blocks, lazors, end_points)
    
