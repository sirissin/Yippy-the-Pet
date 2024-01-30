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

    # Defining how the pet moves
    def move(self, x_amount, y_amount):
        self.x += x_amount
        self.y += y_amount


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
        self.item_mode_index = 0
        self.item = None
        self.apple_button = Item(self.width / 4, self.buttons_bar_height / 2, 0, 0, self.image_names[0])
        self.icecream_button = Item(self.width / 2, self.buttons_bar_height / 2, 0, 0, self.image_names[1])
        self.toy_button = Item(self.width * 3 / 4, self.buttons_bar_height / 2, 0, 0, self.image_names[2])

        # Creating parameters of the pet
        self.pet = Pet(self.width / 2, self.height / 2, 50, 100, 180, 255)
        self.speed = 2
        self.d_x = 0
        self.d_y = 0

    # Checking to see which item has been clicked
    def handle_mouse_click(self):
        pos = pygame.mouse.get_pos()
        if self.apple_button.image_rect.collidepoint(pos):
            self.item_mode_index = 0
        elif self.icecream_button.image_rect.collidepoint(pos):
            self.item_mode_index = 1
        elif self.toy_button.image_rect.collidepoint(pos):
            self.item_mode_index = 2
        # Do nothing if bar is selected (don't place item)
        elif pos[1] < self.buttons_bar_height:
            return
        else:
            self.create_item(pos)

    # Placing down the item
    def create_item(self, pos):
        if self.item_mode_index == 0:
            self.item = Item(pos[0], pos[1], 20, 0, self.image_names[0])
        elif self.item_mode_index == 1:
            self.item = Item(pos[0], pos[1], -10, 60, self.image_names[1])
        elif self.item_mode_index == 2:
            self.item = Item(pos[0], pos[1], 0, 40, self.image_names[2])
        # Setting the pet's speed according to the item
        self.set_speed()

    # Balancing how fast the Pet moves toward the item (so it doesn't move up or sideways quicker than each other)
    def set_speed(self):
        d_x = abs(self.pet.x - self.item.x)
        d_y = abs(self.pet.y - self.item.y)
        if d_x >= d_y:
            self.d_x = self.speed
            self.d_y = self.speed * (d_y / d_x)
        else:
            self.d_x = self.speed * (d_x / d_y)
            self.d_y = self.speed

        # Checking to see if the item is to the left or below the pet
        if self.pet.x > self.item.x:
            self.d_x = -self.d_x
        if self.pet.y > self.item.y:
            self.d_y = -self.d_y

    # Looks for pet/item collision and deletes the item
    def handle_item_collision(self):
        if self.item != None and self.item.image_rect.colliderect(self.pet.get_rect()):
            self.item = None
            self.d_x = 0
            self.d_y = 0

    # Moves the pet
    def update_pet(self):
        self.pet.move(self.d_x, self.d_y)

    def draw_everything(self):
        self.screen.fill(self.background_color)

        # Drawing the buttons bar
        pygame.draw.rect(self.screen, self.buttons_bar_color, pygame.Rect(0, 0, self.width, self.buttons_bar_height))

        # Placing the buttons
        self.screen.blit(self.apple_button.image, self.apple_button.image_rect)
        self.screen.blit(self.icecream_button.image, self.icecream_button.image_rect)
        self.screen.blit(self.toy_button.image, self.toy_button.image_rect)

        # Placing the Items
        if self.item != None:
            self.screen.blit(self.item.image, self.item.image_rect)

        # Placing the Pet
        pygame.draw.circle(self.screen, self.pet.color, self.pet.get_pos(), self.pet.health)

        # Update the Screen
        pygame.display.update()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_click()
            self.handle_item_collision()

            self.update_pet()

            self.draw_everything()
            self.clock.tick(self.clock_tick)


pygame.init()
game = Game()
game.run()
