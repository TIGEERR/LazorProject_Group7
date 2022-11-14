from read_setting import read_setting
from crack_game import main_worker
from visualize_solution import visualize_solution

if __name__=="__main__":
    # Select one board to play
    f = './LazorTemplates/mad_1.bff'

    # Read the setting of the board
    block_grid, blocks, lazors, end_points = read_setting(f)

    # Crack the board
    location_key,lazor_path =  main_worker(block_grid, blocks, lazors, end_points)
    
    # Visualize the solution
    # solution = visualizer_solution(np.shape(block_grid)[1], np.shape(block_grid)[0], 80)
