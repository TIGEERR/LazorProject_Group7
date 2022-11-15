from read_setting import read_setting
from crack_game import main_worker
from visualize_solution import visualizer

if __name__=="__main__":
    # Select one board to play
    f = './LazorTemplates/mad_4.bff'

    # Read the setting of the board
    block_grid, blocks, lazors, end_points = read_setting(f)

    # Crack the board
    location_key,lazor_path =  main_worker(block_grid, blocks, lazors, end_points)
    # print(location_key)

    solution = visualizer(block_grid, 80, location_key, lazor_path, end_points)