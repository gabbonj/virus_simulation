from .. import imports

pygame = imports.pygame

def start_screen():
    scene = imports.settings.main_scene
    pygame.init()
    screen = pygame.display.set_mode((scene.width, scene.height))
    listener_thread = imports.threading.Thread(target=imports.listen_data, daemon=True, name='Listener')
    
    listener_thread.start()


    while imports.settings.running: 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    imports.settings.running = False
            if event.type == pygame.QUIT:
                imports.settings.running = False

        screen.fill(imports.settings.colours['black'])
        scene.update()

        for p in scene.people:

            color = imports.settings.colours['white']
            if p.disease.sickness:
                color = imports.settings.pearson_gradient.get_color(p.disease.percentage)
            else:
                color = imports.settings.colours['green']

            pygame.draw.circle(screen,
                               color,
                               [int(p.position[0]), int(p.position[1])],
                               imports.settings.pearson_size)

        pygame.display.update()
        imports.sleep(.01)