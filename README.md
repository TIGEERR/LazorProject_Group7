# LazorProject_Group7
Codebase for lazor puzzle solver

Author: Anruo Shen, Taichi Liu

# The ideas of the solution:
1. Read the .bff file.
2. Check the 'x' and 'B' positions and pass all avaiable positions to the Solver.
3. List all the combinations of avaiable positions and blocks.
4. Go thourgh all the combinations to find the solutions.
5. Visualize the result.

# Usage:
```
python main.py
```
```
# Enter the puzzle you want to solve
please input the puzzle name: # tiny_5
```
The result will be:
```
A  B  A  
o  o  o  
A  C  o  
```
# Visualization:
|Block Type|Color|
| ---------- | :-----------:  |
| A (Reflect Block)    | Dark  |
| B (Opaque Block)     | Black |
| C (Refract Block)    | Light |

<img src="https://github.com/TIGEERR/LazorProject_Group7/blob/main/Figs/visualize_tiny_5.jpg" width=50% height=50%>
