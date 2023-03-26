"""
Python Data Structures - A Game-Based Approach
DFS maze solver.
Robin Andrews - https://compucademy.net/
The stack contains positions as (row, column) tuples. Predecessors are kept in a dictionary.
"""

from typing import List, Sequence, Tuple, TypeVar, Union
from helpers import get_path, offsets, is_legal_pos, read_maze
from stack import Stack

CHAPTER_PATH = 'D:/05_Further_Learning/Linkedin_Learning/01_Python_Data_Structures_and_Algorithms/04_04_begin'

T = TypeVar("T", str, int)

# Try to implement DFS. 


def dfs(maze: List[List[T]], start: Tuple[int, int], goal: Tuple[int, int]):
    print('=' * 50)
    print(maze)


if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    # assert result == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

    # Test 2
    maze = read_maze(f"{CHAPTER_PATH}/mazes/mini_maze_dfs.txt")
    # for row in maze:
    #     print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    # assert result == [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]

    # Test 3
    maze = read_maze(f"{CHAPTER_PATH}/mazes/mini_maze_dfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = dfs(maze, start_pos, goal_pos)
    # assert result is None
