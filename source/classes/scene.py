from .. import imports


class Scene:

    def __init__(self, width, height, people=[]):
        assert isinstance(people, list)
        assert isinstance(width, int)
        assert isinstance(height, int)
        for p in people:
            assert isinstance(p, imports.Pearson)
        self.people = people
        self.width = width
        self.height = height

    def addPearson(self, pearson):
        assert isinstance(pearson, imports.Pearson)
        self.people.append(pearson)

    def addRandomPeople(self, count):
        for n in range(count):
            newposition = [
                imports.randint(imports.settings.pearson_size, self.width),
                imports.randint(imports.settings.pearson_size, self.height)
            ]
            newvelocity= imports.randint(imports.settings.max_speed, imports.settings.max_speed)
            newangle = imports.randint(0, 360) * 3.14 / 180
            newpeason = imports.Pearson(newposition, newvelocity, newangle)
            self.people.append(newpeason)

    def infectRandom(self, count):
        assert count <= len(self.people)
        for n in range(count):
            self.people[n].infect()

    def avoidCollisions(self):
        for p in self.people:
            a = p.position
            if a[0] > self.width or a[0] < 0 or \
               a[1] > self.height or a[1] < 0:
                p.changeDirection()
            for q in self.people:
                if p == q :
                    continue
                else:
                    b = q.position
                    d = imports.np.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))
                    if d < imports.settings.pearson_size:
                        if d < imports.settings.hibox_radius:
                            p.changeDirection()
                            q.changeDirection()
                        if p.disease.sickness and imports.random() < p.disease.spread_rate:
                            q.infect()
                        if q.disease.sickness and imports.random() < q.disease.spread_rate:
                            p.infect()

    def kill(self):
        for p in self.people:
            if p.disease.percentage >= 1:
                self.people.remove(p)
                print('morto')

    def update(self):
        self.kill()
        self.avoidCollisions()
        for p in self.people:
            p.update()
