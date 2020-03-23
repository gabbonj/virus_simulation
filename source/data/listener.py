from .. import imports

class Listener:

    def __init__(self, scene):
        assert isinstance(scene, imports.Scene)
        self.scene = scene
        self.data = {
            'population' : []
        }
    
    def getPopulation(self):
        return len(self.scene.people)

    def get_data(self):
        current_population = self.getPopulation()
        self.data['population'].append(current_population)

    def update(self):
        self.get_data()