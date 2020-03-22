from .. import imports
from time import sleep 

pygame = imports.pygame

def start_screen(scene):
    assert isinstance(scene, imports.Scene)
    pygame.init()
    screen = pygame.display.set_mode((scene.width, scene.height))
    imports.settings.running = True

    while imports.settings.running: 

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    imports.settings.running = False
            if event.type == pygame.QUIT:
                imports.settings.running = False

        screen.fill(imports.settings.colours['black'])

        for p in scene.people:

            color = imports.settings.colours['white']
            if p.disease.sickness:
                color = imports.settings.colours['red']
            else:
                color = imports.settings.colours['green']

            pygame.draw.circle(screen,
                               color,
                               p.position,
                               imports.settings.pearson_size)

        pygame.display.update()
        scene.update()
        sleep(.01)
