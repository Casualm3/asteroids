import pygame
from circleshape import CircleShape
class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.screen = None

    def draw(self, screen):
        pygame.draw.circle(screen, (225, 225, 225), (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt