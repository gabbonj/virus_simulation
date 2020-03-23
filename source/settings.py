from .classes.gradient import Gradient

colours = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255)
}
data = {}
running = False
main_scene = None
sample_rate = 1

pearson_gradient = Gradient(colours['green'], colours['red'])
max_direction_scatter = .1
pearson_size = 5
hibox_radius = 3
max_speed = 2
min_speed = 0
disease_evolution = .05