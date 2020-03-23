from .. import imports


class Pearson:

    def __init__(self, position, velocity, angle, health=None, disease=None):
        self.position = position
        self.velocity = velocity
        self.angle = angle
        if health == None:
            self.health = imports.Health()
        else:
            assert isinstance(health, imports.Health)
            self.health = health
        if disease == None:
            self.disease = imports.Disease()
        else:
            assert isinstance(disease, imports.Disease)
            self.disease = disease
            
    def infect(self):
        self.disease.sickness = True

    def changeDirection(self):
        self.angle = (self.angle + 3.14 + imports.settings.max_direction_scatter * imports.random()) % 6.28
        self.position[0] += imports.np.sin(self.angle) * imports.settings.pearson_size
        self.position[1] += imports.np.cos(self.angle) * imports.settings.pearson_size
    
    def update(self):
        random_factor = imports.random()

        move = imports.np.array([
            imports.np.sin(self.angle) * self.velocity,
            imports.np.cos(self.angle) * self.velocity
        ])
        newposition = imports.np.array(self.position) + move
        self.position = newposition.astype('int64').tolist()

        if self.disease.sickness:
            if random_factor > self.health.strongness:
                self.disease.percentage += imports.settings.disease_evolution
            else:
                self.disease.percentage -= imports.settings.disease_evolution

            if self.disease.percentage > 1:
                self.disease.percentage = 1
            elif self.disease.percentage <= 0:
                self.disease.spread_rate = imports.settings.spread_rate_calback
                self.disease.percentage = imports.settings.disease_callback
                self.disease.sickness = False
                self.health.strongness += imports.settings.health_callback
                print('guarito')