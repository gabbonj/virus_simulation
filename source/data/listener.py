from .. import imports

class Listener:

    def __init__(self, scene):
        assert isinstance(scene, imports.Scene)
        self.scene = scene
        self.data = {
            'population' : [],
            'mean velocity' : []
        }
    
    def getPopulation(self):
        return len(self.scene.people)

    def getMeanVelocity(self):
        mean = 0
        for p in self.scene.people:
            mean += p.velocity
        return mean/ len(self.scene.people)

    def get_data(self):
        current_population = self.getPopulation()
        self.data['population'].append(current_population)
        current_mean_velocity = self.getMeanVelocity()
        self.data['mean velocity'].append(current_mean_velocity)

    def update(self):
        self.get_data()