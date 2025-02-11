import pygame  # type: ignore
from maze_generation import generate_maze, display_maze_with_colors, add_start_and_end_points

def ai_solve_maze(maze, start, end):
    """
    AI solves the maze using Breadth-First Search (BFS).
    Returns steps and the path taken, or indicates no solution.
    """
    from queue import Queue

    queue = Queue()
    queue.put((start, [start]))
    visited = set()
    visited.add(start)
    while not queue.empty():
        '''Based on difficulty parameter adjust time.sleep time'''
        current, path = queue.get()
        if current == end:
            return len(path) - 1, path  # Return the steps and path

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = current[0] + dx, current[1] + dy
            if (0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and
                    maze[nx][ny] == 0 and (nx, ny) not in visited):
                queue.put(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))

    return float('inf'), []  # Return the empty path if no solution is found


def ai_only_mode(screen, settings):
    width, height = settings.maze_size
    cell_size = min(600 // width, 600 // height)  # Dynamic cell size
    maze = generate_maze(width, height)
    start, end = (1, 1), (height - 3, width - 3)
    print(maze, start, end)
    steps, path = ai_solve_maze(maze, start, end)

    if not path:
        print("No solution found by AI.")
        return

    # Visualize AI solving the maze
    for pos in path:
        screen.fill((0, 0, 0))
        display_maze_with_colors(screen, maze, cell_size, settings.selected_wall_color)
        add_start_and_end_points(screen, maze, cell_size, start_color=(0, 255, 0), end_color=(255, 0, 0))
        x, y = pos[1] * cell_size, pos[0] * cell_size
        pygame.draw.rect(screen, (0, 255, 0), (x, y, cell_size, cell_size))  # Green path
        pygame.display.flip()
        pygame.time.delay(100)

    print(f"AI Steps: {steps}, Time: {steps * 0.1:.2f} seconds")
