# File: fifteen_puzzle.py

from typing import Optional
from generic_search import astar, Node, node_to_path

Frame = tuple[tuple[int, ...], ...]

def goal_test(frame: Frame) -> bool:
    """Is this the goal frame?"""
    flat: tuple[int, ...] = tuple(i for tup in frame for i in tup)
    goal: tuple[int, ...] = tuple(range(1, len(flat))) + (0,)
    return flat == goal  # type: ignore


def successors(frame: Frame) -> list[Frame]:
    """Return a list of valid successors to this frame."""
    flat: tuple[int, ...] = tuple(i for tup in frame for i in tup)
    rows = len(frame)
    columns = len(frame[0])
    zero_index: int = flat.index(0)
    
    def swap(i1: int, i2: int) -> Frame:
        """Swap the values at the given indices."""
        lst: list[int] = list(flat)
        lst[i1], lst[i2] = lst[i2], lst[i1]
        return tuple(tuple(lst[r * columns:(r + 1) * columns])
                     for r in range(rows))
        
    # Generate potential successors
    up = swap(zero_index, zero_index - columns) if zero_index >= columns else None
    down = swap(zero_index, zero_index + columns) if zero_index + columns < len(flat) else None
    left = swap(zero_index, zero_index - 1) if zero_index % columns != 0 else None
    right = swap(zero_index, zero_index + 1) if (zero_index + 1) % columns != 0 else None
    
    return [s for s in (up, down, left, right) if s is not None]


def heuristic(frame: Frame) -> float:
    """Return the heuristic value for a given frame."""
    flat: tuple[int, ...] = tuple(i for tup in frame for i in tup)
    goal: tuple[int, ...] = tuple(range(1, len(flat))) + (0,)
    
    return float(sum(1 for i, j in zip(flat, goal) if i != j))


def solve_puzzle(frame: Frame) -> None:
    """Solve the fifteen puzzle game."""
    
    result: Optional[Node[Frame]] = astar(
        frame, goal_test, successors, heuristic)
    
    if result is None:
        print('No solution found!')
    else:
        path = node_to_path(result)
        if len(path) - 2 == 0:
            print(f'Solution requires {len(path)-1} step')
        else:
            print(f'Solution requires {len(path) - 1} steps')

        for i in range(len(path)-1):
            flat: tuple[int, ...] = tuple(k for tup in path[i] for k in tup)
            flat_next: tuple[int, ...] = tuple(k for tup in path[i+1] for k in tup)
            
            columns = len(frame[0])
            zero_index: int = flat.index(0)
            zero_index_next: int = flat_next.index(0)
            
            movement = ""
            if zero_index_next == zero_index - columns:
                movement = "down"
            elif zero_index_next == zero_index + columns:
                movement = "up"
            elif zero_index_next == zero_index - 1:
                movement = "right"
            elif zero_index_next == zero_index + 1:
                movement = "left"
            
            print(f'Step {i+1}: Move {flat_next[zero_index]} {movement}')
            
            
if __name__ == "__main__":
    solve_puzzle(((2, 3, 4, 8),
                      (1, 5, 7, 11),
                      (9, 6, 12, 15),
                      (13, 14, 10, 0)))
    