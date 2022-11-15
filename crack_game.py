from utils import ReflectBlock, RefractBlock, OpaqueBlock, Grid, Lazor
from copy import deepcopy
from tqdm import tqdm
from sympy.utilities.iterables import multiset_permutations


class Solver():

    def __init__(self, grids, lazors, blocks, end_points):
        self.all_PosBlock, self.grid = grids()
        self.saved_blocks = set()

        self.lazors = lazors
        self.blocks = blocks
        self.end_points = end_points

    def add_block(self, pos_block, grid):
        for block_type, pos in pos_block:
            grid[pos[1]][pos[0]]= block_type
        return grid

    def pos_chk(self, lazor):
        if lazor.x+ lazor.vx < 0 or lazor.x+ lazor.vx > len(self.grid[0]) - 1 or lazor.y+ lazor.vy < 0 or lazor.y+ lazor.vy > len(self.grid) - 1:
            return False
        else:
            return True

    def solve(self):
        solved = False
        block_list = []
        if self.blocks['A'] > 0:
            for i in range(self.blocks['A']):
                block_list.append('A')
        if self.blocks['B'] > 0:
            for i in range(self.blocks['B']):
                block_list.append('B')
        if self.blocks['C'] > 0:
            for i in range(self.blocks['C']):
                block_list.append('C')

        print('Prepare possible positions for blocks')
        # pos_blocks = [''.join(i) for i in multiset_permutations(''.join(block_list)+'o'*(len(self.all_PosBlock)-len(block_list)))]
        pos_blocks =  [i for i in multiset_permutations(block_list+['o']*(len(self.all_PosBlock)-len(block_list)))]

        for pos_block in tqdm(pos_blocks):
            solved_lazor = []
            pos_block = list(zip(pos_block, self.all_PosBlock))
            tmp_grid = self.add_block(pos_block, deepcopy(self.grid))
            lazors = deepcopy(self.lazors)
            end_points = deepcopy(self.end_points)
            for lazor in lazors:
                while self.pos_chk(lazor) and lazor.blocking == False and lazor.dead == False:
                    if (tmp_grid[lazor.y][lazor.x + lazor.vx] == 'o' or tmp_grid[lazor.y][lazor.x + lazor.vx] == 'x') and (tmp_grid[lazor.y + lazor.vy][lazor.x] == 'o' or tmp_grid[lazor.y + lazor.vy][lazor.x] == 'x'):
                        lazor()
                    else:
                        block_x = lazor.x + lazor.vx
                        block_y = lazor.y
                        if tmp_grid[block_y][block_x] == 'o':
                            block_x = lazor.x
                            block_y = lazor.y + lazor.vy

                        if tmp_grid[block_y][block_x] == 'A':
                            block = ReflectBlock(block_x, block_y)
                            lazor = block(lazor)
                        if tmp_grid[block_y][block_x] == 'B':
                            block = OpaqueBlock(block_x, block_y)
                            lazor = block(lazor)
                        if tmp_grid[block_y][block_x] == 'C':
                            block = RefractBlock(block_x, block_y)
                            new_lazor, lazor = block(lazor)
                            lazors.append(new_lazor)

                    if (lazor.x, lazor.y) in end_points:
                        end_points.remove((lazor.x, lazor.y))

                solved_lazor.append(lazor.path)
            ## end
            if len(end_points) == 0:
                solved = True
                break

        result_block_type = []
        result_pos = []
        for block_type, pos in pos_block:
            result_block_type.append((block_type))
            # result_pos.append(((pos[0]-1)//2, (pos[1]-1)//2))
            result_pos.append(((pos[0]-1)//2, (pos[1]-1)//2))
        return solved, result_block_type, result_pos, solved_lazor
                

def plot_result(Grids, types, pos):
    block_grid = Grids.block_grid
    for i in range(len(block_grid)):
        for j in range(len(block_grid[0])):
            if (j,i) in pos:
                print(types[pos.index((j,i))], end='  ')
            elif block_grid[i][j] == 'B':
                print('B', end='  ')
            elif block_grid[i][j] == 'o':
                print('o', end='  ')
            elif block_grid[i][j] == 'x':
                print('x', end='  ')
        print('')


    
def main_worker(block_grid, blocks, lazors, end_points):
    Grids = Grid(block_grid)
    lazors = [Lazor(**lazor) for lazor in lazors]
    solver = Solver(Grids, lazors, blocks, end_points)
    solved, result_block_type, result_pos, solved_lazor = solver.solve()
    if solved:
        plot_result(Grids, result_block_type, result_pos)
    else:
        print('No answer.')

    key = (list(zip(result_block_type, result_pos)))

    return key, solved_lazor