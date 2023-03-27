"""
Python Data Structures - A Game-Based Approach
DFS maze solver.
Robin Andrews - https://compucademy.net/
The stack contains positions as (row, column) tuples. Predecessors are kept in a dictionary.
"""

from typing import List, Optional, Tuple, TypeVar
from helpers import get_path, offsets, is_legal_pos, read_maze
from stack import Stack

CHAPTER_PATH = 'D:/05_Further_Learning/Linkedin_Learning/01_Python_Data_Structures_and_Algorithms/04_04_begin'

T = TypeVar("T", str, int)


def dfs(maze: List[List[T]], start: Tuple[int, int], goal: Tuple[int, int]) -> Optional[List[List[Tuple[int, int]]]]:
    result = None

    stack = Stack()
    stack.push(start)
    predecessors = {start: None}

    while not stack.is_empty():
        current_point = stack.pop()
        if current_point == goal:


            # Start by understanding get_path function

            result = get_path(predecessors, start, goal)
        else:
            for neighbour_pos in ['up', 'right', 'down', 'left']:
                row_offset, column_offset = offsets[neighbour_pos]
                neighbour_point = (current_point[0] + row_offset, current_point[1] + column_offset)
                if is_legal_pos(maze, neighbour_point) and neighbour_point not in predecessors:
                    stack.push(neighbour_point)
                    predecessors[neighbour_point] = current_point

    return result


if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

    # Test 2
    maze = read_maze(f"{CHAPTER_PATH}/mazes/mini_maze_dfs.txt")
    # for row in maze:
    #     print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]

    # Test 3
    maze = read_maze(f"{CHAPTER_PATH}/mazes/mini_maze_dfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = dfs(maze, start_pos, goal_pos)
    assert result is None
