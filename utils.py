class Grid():
    def __init__(self, block_grid):
        self.block_grid = block_grid
        grid = [
            ['o' for i in range(2 * len(self.block_grid[0]) + 1)]
            for j in range(2 * len(self.block_grid) + 1)
        ]
        for i in range(len(self.block_grid)):
            for j in range(len(self.block_grid[i])):
                if self.block_grid[i][j] == 'x':
                    grid[2 * i + 1][2 * j + 1] = 'x'
                elif self.block_grid[i][j] == 'B':
                    grid[2 * i + 1][2 * j + 1] = 'B'
        self.grid = grid

    def __call__(self):
        pos_blocks = []
        pos_non_blocks = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 'o' and i % 2 != 0 and j % 2 != 0:
                    ## reverse i and j
                    pos_blocks.append((j, i))
                elif self.grid[i][j] == 'x' and i % 2 != 0 and j % 2 != 0:
                    pos_non_blocks.append(('x', (j, i)))
                elif self.grid[i][j] == 'B' and i % 2 != 0 and j % 2 != 0:
                    pos_non_blocks.append(('B', (j, i)))
        return pos_blocks, pos_non_blocks, self.grid

class Lazor():
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.blocking = False
        self.dead = False
        self.path = []
        self.add_path(self.x, self.y)

    def __str__(self):
        return "Lazor_x, Lazor_y, Lazor_vx, Lazor_vy, Lazor_blocking, Lazor_path: " + str(self.x) + ', ' + str(self.y) \
                +  ', ' + str(self.vx) + ', ' + str(self.vy)+ ', ' + str(self.blocking) + ', ' + str(self.path)

    def add_path(self, x, y):
        if self.path.count((x,y)) > 2:
            self.dead = True
        self.path.append((x, y))

    def __call__(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.add_path(self.x, self.y)

class ReflectBlock():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "ReflectBlock_x, ReflectBlock_y: " + str(self.x) + ', ' + str(self.y)

    def reflect(self, lazor):
        lazor_x = lazor.x
        lazor_y = lazor.y
        lazor_vx = lazor.vx
        lazor_vy = lazor.vy
        # left or right
        if (self.x - 1, self.y) == (lazor_x, lazor_y) or (self.x + 1, self.y) == (lazor_x, lazor_y):
            lazor_x = lazor_x - lazor_vx
            lazor_y = lazor_y + lazor_vy
            lazor_vx = -lazor_vx
        # up or down
        if (self.x, self.y - 1) == (lazor_x, lazor_y) or (self.x, self.y + 1) == (lazor_x, lazor_y):
            lazor_x = lazor_x + lazor_vx
            lazor_y = lazor_y - lazor_vy
            lazor_vy = -lazor_vy

        return lazor_x, lazor_y, lazor_vx, lazor_vy
    
    def __call__(self, lazor):
        lazor.x, lazor.y, lazor.vx, lazor.vy = self.reflect(lazor)
        lazor.add_path(lazor.x, lazor.y)
        return lazor

class OpaqueBlock():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "OpaqueBlock_x, OpaqueBlock_y: " + str(self.x) + ', ' + str(self.y)

    def Opaque(self, lazor):
        lazor.blocking = True
        return lazor
    
    def __call__(self, lazor):
        return self.Opaque(lazor)

    


class RefractBlock():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "RefractBlock_x, RefractBlock_y: " + str(self.x) + ', ' + str(self.y)

    def reflect(self, lazor):
        lazor_x = lazor.x
        lazor_y = lazor.y
        lazor_vx = lazor.vx
        lazor_vy = lazor.vy
        # left or right
        if (self.x - 1, self.y) == (lazor_x, lazor_y) or (self.x + 1, self.y) == (lazor_x, lazor_y):
            lazor_x = lazor_x - lazor_vx
            lazor_y = lazor_y + lazor_vy
            lazor_vx = -lazor_vx
        # up or down
        if (self.x, self.y - 1) == (lazor_x, lazor_y) or (self.x, self.y + 1) == (lazor_x, lazor_y):
            lazor_x = lazor_x + lazor_vx
            lazor_y = lazor_y - lazor_vy
            lazor_vy = -lazor_vy

        return lazor_x, lazor_y, lazor_vx, lazor_vy

    def refract(self, lazor):
        new_x, new_y, new_vx, new_vy = self.reflect(lazor)
        new_lazor = Lazor(lazor.x, lazor.y, new_vx, new_vy)
        lazor()
        return new_lazor, lazor

    def __call__(self, lazor):
        return self.refract(lazor)





if __name__=="__main__":
    from read_setting import read_setting

    # f = './LazorTemplates/mad_1.bff'
    f = './LazorTemplates/dark_1.bff'
    block_grid, blocks, lazor, end_point = read_setting(f)
    Grid = Grid(block_grid)
    print(Grid())