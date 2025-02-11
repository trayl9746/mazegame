import pygame  # type: ignore
import time
from maze_generation import generate_maze, display_maze_with_colors, add_start_and_end_points
from aionly_mode import ai_solve_maze

def generate_solvable_maze(width, height, start, end):
    """
    Generate a maze that is guaranteed to be solvable.
    """
    while True:
        maze = generate_maze(width, height)
        _, path = ai_solve_maze(maze, start, end)
        if path:  # Check if a valid path exists
            return maze, path


def player_vs_ai_mode(screen, settings):
    width, height = settings.maze_size
    cell_size = min(600 // width, 600 // height)  # Dynamic cell size
    start, end = (1, 1), (height - 3, width - 3)
    maze, ai_path = generate_solvable_maze(width, height, start, end)

    if not ai_path:
        print("No solution found by AI.")
        return

    # Initialize positions
    player_pos = list(start)
    ai_index = 0
    player_steps, ai_steps = 0, 0
    timer_duration = 40
    start_time = time.time()

    running = True
    while running:
        elapsed_time = time.time() - start_time
        time_left = max(0, timer_duration - elapsed_time)

        if time_left <= 0:
            print("Time's up!")
            break

        # Player movement (keyboard input)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                new_pos = player_pos[:]
                if event.key == pygame.K_UP:
                    new_pos[0] -= 1
                elif event.key == pygame.K_DOWN:
                    new_pos[0] += 1
                elif event.key == pygame.K_LEFT:
                    new_pos[1] -= 1
                elif event.key == pygame.K_RIGHT:
                    new_pos[1] += 1

                if (0 <= new_pos[0] < height and 0 <= new_pos[1] < width and
                        maze[new_pos[0]][new_pos[1]] == 0):
                    player_pos = new_pos
                    player_steps += 1

        # AI movement
        if ai_index < len(ai_path) - 1:
            ai_index += 1
            ai_steps += 1

        # Check if game is over
        if tuple(player_pos) == end:
            running = False
            #print how much time it took for the player

        # Render maze
        screen.fill((0, 0, 0))
        display_maze_with_colors(screen, maze, cell_size, settings.selected_wall_color)
        add_start_and_end_points(screen, maze, cell_size, start_color=(0, 255, 0), end_color=(255, 0, 0))
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(player_pos[1] * cell_size, player_pos[0] * cell_size, cell_size, cell_size))  # Player
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(ai_path[ai_index][1] * cell_size, ai_path[ai_index][0] * cell_size, cell_size, cell_size))  # AI

        # Timer and steps
        font = pygame.font.Font(None, 36)
        timer_text = font.render(f"Time Left: {time_left:.1f}s", True, (255, 255, 255))
        steps_text = font.render(f"Player Steps: {player_steps}", True, (255, 255, 255))
        screen.blit(timer_text, (10, 10))
        screen.blit(steps_text, (10, 50))

        pygame.display.flip()

    print(f"Player Steps: {player_steps}, AI Steps: {ai_steps}")
    

