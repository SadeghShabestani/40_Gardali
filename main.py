import pygame
import random
import time


class Color:
    bg = (186, 176, 149)
    yellow = (212, 203, 34)
    blue = (51, 61, 245)
    green = (50, 230, 92)
    orange = (196, 118, 27)
    pink = (223, 117, 235)


class Gardali:
    images = ['pic/watermelon.png', 'pic/banana.png', 'pic/cherries.png', 'pic/pear.png', 'pic/strawberry.png']

    def __init__(self):
        self.radius = 50
        self.x = random.randint(0, Game.width - self.radius)
        self.y = random.randint(0, Game.height - self.radius)
        self.color = random.choice([Color.yellow, Color.blue, Color.green, Color.orange, Color.pink])
        self.image_path = random.choice(Gardali.images)
        self.image = pygame.image.load(self.image_path)
        self.image2 = pygame.transform.scale(self.image, (90, 90))
        self.score = 0
        self.area = pygame.draw.circle(Game.window, self.color, (self.x, self.y), self.radius)

    def show(self):
        self.area = pygame.draw.circle(Game.window, self.color, (self.x, self.y), self.radius)
        Game.window.blit(self.image2, (self.x - self.radius, self.y - self.radius))

    def move(self):
        self.x = random.randint(0, Game.width - self.radius)
        self.y = random.randint(0, Game.height - self.radius)


class Game:
    pygame.init()
    width = 800
    height = 600
    window = pygame.display.set_mode((width, height))
    font = pygame.font.Font(None, 40)
    start_time = 0
    total_time = 0
    clock = pygame.time.Clock()
    fps = 30

    @staticmethod
    def time():
        Game.total_time = time.time() - Game.start_time
        text = Game.font.render(f"Time: {round(Game.total_time)}", True, (0, 0, 0))
        Game.window.blit(text, (0, 0))

    @staticmethod
    def play():
        Game.start_time = time.time()
        gardalis = [Gardali()]
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for gardali in gardalis:
                        if gardali.area.collidepoint(event.pos):
                            if gardali == gardalis[-1]:
                                temp = Gardali()
                                while True:
                                    # if not any(temp.image_path == gardali.image_path and temp.color == gardali.color for gardali in gardalis):
                                    if all(g.image_path != temp.image_path or g.color != temp.color for g in gardalis):
                                        gardalis.append(temp)

                                        break

                            else:

                                Game.play()
                        gardali.move()

            Game.window.fill(Color.bg)

            for gardali in gardalis:
                gardali.show()
                Game.time()
            pygame.display.update()
            Game.clock.tick(Game.fps)


if __name__ == '__main__':
    Game.play()
