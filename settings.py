import pygame # type: ignore

class GameSettings:
    """
    Class to manage game settings such as difficulty levels, maze size, and wall color.
    """
    def __init__(self):
        self.difficulty_levels = {
            "Beginner": (15, 15),
            "Experienced": (20, 20),
            "Advanced": (25, 25),
            "Expert": (30, 30),
            "Ultimate": (40, 40),
        }
        self.current_difficulty = "Beginner"
        self.maze_size = self.difficulty_levels[self.current_difficulty]
        self.selected_wall_color = (0, 0, 0)  # Default to white walls

    def set_difficulty(self, difficulty):
        """
        Set the game difficulty and update the maze size.
        """
        if difficulty in self.difficulty_levels:
            self.current_difficulty = difficulty
            self.maze_size = self.difficulty_levels[difficulty]
            print(f"Difficulty set to {difficulty}. Maze size: {self.maze_size}")
        else:
            print("Invalid difficulty level. Choose from:", list(self.difficulty_levels.keys()))

    def set_wall_color(self, color):
        """
        Set the wall color of the maze.
        """
        self.selected_wall_color = color
        print(f"Wall color set to: {color}")

def configure_settings(screen, bg_image, settings):
    """
    Settings menu to allow the player to adjust game settings with options for each category.
    """
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    menu_options = [
        "Change Difficulty",
        "Change Wall Color",
        "Back to Main Menu",
    ]

    running = True
    while running:
        screen.blit(bg_image, (0, 0))  # Draw the background
        mouse_pos = pygame.mouse.get_pos()

        for i, option in enumerate(menu_options):
            text = font.render(option, True, (255, 255, 255))
            rect = text.get_rect(center=(400, 150 + i * 100))
            pygame.draw.rect(screen, (50, 50, 50), rect.inflate(20, 10), border_radius=10)
            if rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, (100, 100, 100), rect.inflate(20, 10), border_radius=10)
            screen.blit(text, rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, option in enumerate(menu_options):
                    rect = pygame.Rect(400 - 100, 150 + i * 100 - 20, 200, 40)
                    if rect.collidepoint(event.pos):
                        if i == 0:  # Change Difficulty
                            select_difficulty(screen, bg_image, settings)
                        elif i == 1:  # Set Custom Maze Size
                            select_wall_color(screen, bg_image, settings)
                        elif i == 3:  # Back to Main Menu
                            running = False  # Exit to main menu

def select_difficulty(screen, bg_image, settings):
    """
    Allow the player to choose the game difficulty level.
    """
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    difficulties = list(settings.difficulty_levels.keys()) + ["Go Back to Settings"]

    running = True
    while running:
        screen.blit(bg_image, (0, 0))  # Draw background
        mouse_pos = pygame.mouse.get_pos()

        for i, difficulty in enumerate(difficulties):
            text = font.render(difficulty, True, (255, 255, 255))
            rect = text.get_rect(center=(400, 150 + i * 100))
            pygame.draw.rect(screen, (50, 50, 50), rect.inflate(20, 10), border_radius=10)
            if rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, (100, 100, 100), rect.inflate(20, 10), border_radius=10)
            screen.blit(text, rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, difficulty in enumerate(difficulties):
                    rect = pygame.Rect(400 - 100, 150 + i * 100 - 20, 200, 40)
                    if rect.collidepoint(event.pos):
                        if difficulty == "Go Back to Settings":
                            running = False  # Return to settings menu
                        else:
                            settings.set_difficulty(difficulty)
                            print(f"Difficulty Set to: {difficulty}")
                            running = False  # Return to settings menu



def select_wall_color(screen, bg_image, settings):
    """
    Allow the player to choose a wall color for the maze.
    """
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    colors = {
        "Red": (255, 0, 0),
        "Green": (0, 255, 0),
        "Blue": (0, 0, 255),
        "Yellow": (255, 255, 0),
        "White": (255, 255, 255),
    }
    color_names = list(colors.keys()) + ["Go Back to Settings"]

    running = True
    while running:
        screen.blit(bg_image, (0, 0))  # Draw background
        mouse_pos = pygame.mouse.get_pos()

        for i, color_name in enumerate(color_names):
            text_color = colors[color_name] if color_name != "Go Back to Settings" else (255, 255, 255)
            text = font.render(color_name, True, text_color)
            rect = text.get_rect(center=(400, 150 + i * 100))
            pygame.draw.rect(screen, (50, 50, 50), rect.inflate(20, 10), border_radius=10)
            if rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, (100, 100, 100), rect.inflate(20, 10), border_radius=10)
            screen.blit(text, rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, color_name in enumerate(color_names):
                    rect = pygame.Rect(400 - 100, 150 + i * 100 - 20, 200, 40)
                    if rect.collidepoint(event.pos):
                        if color_name == "Go Back to Settings":
                            running = False  # Return to settings menu
                        else:
                            settings.set_wall_color(colors[color_name])
                            print(f"Wall Color Set to: {color_name}")
                            running = False  # Return to settings menu
