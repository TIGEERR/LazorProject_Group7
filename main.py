from read_setting import read_setting
from crack_game import main_worker
from visualize_solution import visualizer


if __name__=="__main__":
    f = './LazorTemplates/yarn_5.bff'
    block_grid, blocks, lazors, end_points = read_setting(f)
    location_key, lazor_path = main_worker(block_grid, blocks, lazors, end_points)
    solution = visualizer(block_grid, 80, location_key, lazor_path, end_points, lazors)