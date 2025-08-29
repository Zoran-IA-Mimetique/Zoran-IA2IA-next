
from collections import deque

def solve_maze(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    visited = set([start])
    queue = deque([(start, [start])])
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == goal:
            return path
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny]==0 and (nx,ny) not in visited:
                visited.add((nx,ny))
                queue.append(((nx,ny), path+[(nx,ny)]))
    return None

if __name__ == "__main__":
    maze = [[0,1,0,0],
            [0,1,0,1],
            [0,0,0,0],
            [1,1,1,0]]
    start, goal = (0,0),(3,3)
    print(solve_maze(maze, start, goal))
