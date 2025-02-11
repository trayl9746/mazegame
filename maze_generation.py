import pygame # type: ignore
import random
import numpy as np # type: ignore

def generate_maze(width, height):
    """
    Generate a randomized maze using Depth-First Search (DFS).
    """
    maze = np.ones((height, width), dtype=int)

    def dfs(x, y):
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < height - 1 and 0 < ny < width - 1 and maze[nx, ny] == 1:
                maze[nx, ny] = 0
                maze[x + dx // 2, y + dy // 2] = 0
                dfs(nx, ny)

    start_x, start_y = random.randint(1, height // 2) * 2 - 1, random.randint(1, width // 2) * 2 - 1
    maze[start_x, start_y] = 0
    dfs(start_x, start_y)

    return maze

def display_maze_with_colors(screen, maze, cell_size, wall_color=(0, 0, 0), path_color=(255, 255, 255)):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            color = path_color if maze[row][col] == 0 else wall_color
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))


def add_start_and_end_points(screen, maze, cell_size, start_color=(0, 255, 0), end_color=(255, 0, 0)):
    """
    Add start and end points to the maze.

    Args:
        screen: The Pygame screen to draw on.
        maze: The maze array.
        cell_size: The size of each cell in the maze.
        start_color: The color of the start point.
        end_color: The color of the end point.
    """
    start = (1, 1)  # Start point
    end = (len(maze) - 3, len(maze[0]) - 3)  # End point

    # Draw start point
    pygame.draw.rect(
        screen,
        start_color,
        (start[1] * cell_size, start[0] * cell_size, cell_size, cell_size),
    )

    # Draw end point
    pygame.draw.rect(
        screen,
        end_color,
        (end[1] * cell_size, end[0] * cell_size, cell_size, cell_size),
    )
