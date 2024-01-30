import pygame

# Pet class
class Pet:

    # Parameters of the pet
    def __init__(self, x, y, health, max_health, happiness, max_happiness):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = max_health
        self.happiness = happiness
        self.max_happiness = max_happiness

        # Color will change shade of green depending on happiness
        self.color = pygame.Color(0, happiness, 0)

    # Getting the coordinates of the pet
    def get_pos(self):
        return pygame.Vector2(self.x, self.y)

    # Defining the hit box of the pet
    def get_rect(self):
        return pygame.Rect(self.x - self.health, self.y - self.health, self.health * 2, self.health * 2)


# Class for items/buttons
class Item:

    def __init__(self, x, y, health, happiness, image_name):
        self.x = x
        self.y = y
        self.health = health
        self.happiness = happiness
        self.image = pygame.image.load(image_name)
        rect = self.image.get_rect()
        # Written so the center of the image is where the user clicks
        self.image_rect = pygame.Rect(x - rect.width / 2, y - rect.height / 2, rect.width, rect.height)


class Game:

    def __init__(self):
        # Display Screen properties
        self.width = 500
        self.height = 500
        self.background_color = "white"

        # Buttons bar parameters
        self.buttons_bar_height = 100
        self.buttons_bar_color = "orange"

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Yippy the Pet")

        self.clock_tick = 60
        self.clock = pygame.time.Clock()

        # Creating the parameters of the buttons
        self.image_names = ["apple.png", "icecream.png", "toy.png"]
        self.apple_button = Item(self.width / 4, self.buttons_bar_height / 2, 0, 0, self.image_names[0])
        self.icecream_button = Item(self.width / 2, self.buttons_bar_height / 2, 0, 0, self.image_names[1])
        self.toy_button = Item(self.width * 3 / 4, self.buttons_bar_height / 2, 0, 0, self.image_names[2])

    def draw_everything(self):
        self.screen.fill(self.background_color)

        # Drawing the buttons bar
        pygame.draw.rect(self.screen, self.buttons_bar_color, pygame.Rect(0, 0, self.width, self.buttons_bar_height))

        # Placing the buttons
        self.screen.blit(self.apple_button.image, self.apple_button.image_rect)
        self.screen.blit(self.icecream_button.image, self.icecream_button.image_rect)
        self.screen.blit(self.toy_button.image, self.toy_button.image_rect)

        # Update the Screen
        pygame.display.update()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.draw_everything()
            self.clock.tick(self.clock_tick)

pygame.init()
game = Game()
game.run()
