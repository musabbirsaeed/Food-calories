import sys
from render_canvas import *
from pygame.locals import *


class Scene1:

    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.image = pygame.image.load(os.path.join('data', 'background.png'))
        self.logo = pygame.image.load(os.path.join('data', 'white-logo.png')).convert_alpha()
        self.button = Button(350, 70, (width - 350) // 2, 450, 0, 1, canvas, "", 255, "", 0)
        self.activate = True
        self.width = width
        self.height = height

    def render(self):
        display_image(self.image, 0, 0, self.width, self.height, self.canvas)
        display_image(self.logo, (self.width - self.logo.get_width()) // 2,
                      (self.height - self.logo.get_height()) // 2 - 50, self.logo.get_width(),
                      self.logo.get_height(), self.canvas)
        self.button.render()
        display_text_middle(None, 30, "Create new profile!", (255, 255, 255), self.canvas, self.button)

    def active(self):
        if self.activate:
            fps_clock = pygame.time.Clock()
            mouse_pos = (0, 0)
            scene1_render = True
            while scene1_render:
                self.render()
                act = self.button.activate(mouse_pos)
                if act:
                    pygame.mouse.set_cursor(*pygame.cursors.diamond)
                else:
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                        pygame.quit()
                        sys.exit()
                    elif event.type == MOUSEBUTTONUP and act:
                        scene1_render = False
                    elif event.type == MOUSEMOTION:
                        mouse_pos = pygame.mouse.get_pos()
                pygame.display.update()
                fps_clock.tick(200)


width1 = 1327
height1 = 700
pygame.init()
display_surf = pygame.display.set_mode((width1, height1))
scene1 = Scene1(display_surf, width1, height1)
scene1.active()
