import random
import pygame

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.agent_position = (0, 0)
        self.food_position = (random.randint(0, width - 1), random.randint(0, height - 1))

        pygame.init()
        self.cell_size = 20
        self.screen = pygame.display.set_mode((self.width * self.cell_size, self.height * self.cell_size))
        pygame.display.set_caption('Environment')
        self.screen.fill((255, 255, 255))

    def reset(self):
        self.agent_position = (0, 0)
        self.food_position = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
        return self.agent_position

    def step(self, action):
        x, y = self.agent_position
        if action == 'up' and y > 0:
            y -= 1
        elif action == 'down' and y < self.height - 1:
            y += 1
        elif action == 'left' and x > 0:
            x -= 1
        elif action == 'right' and x < self.width - 1:
            x += 1
        self.agent_position = (x, y)
        self.calculate_reward()
        return self.agent_position

    def render(self):
        self.screen.fill((255, 255, 255))
        agent_rect = pygame.Rect(self.agent_position[0] * self.cell_size, self.agent_position[1] * self.cell_size, self.cell_size, self.cell_size)
        pygame.draw.rect(self.screen, (0, 0, 255), agent_rect)

        food_rect = pygame.Rect(self.food_position[0] * self.cell_size, self.food_position[1] * self.cell_size, self.cell_size, self.cell_size)
        pygame.draw.rect(self.screen, (255, 0, 0), food_rect)

        pygame.display.flip()
        pygame.time.wait(500)

    def calculate_reward(self):
        if self.agent_position == self.food_position:
            return 1
        return 0

# Example usage
if __name__ == "__main__":
    env = Environment(25, 25)
    env.render()
    env.step('right')
    env.render()
    env.step('down')
    env.render()