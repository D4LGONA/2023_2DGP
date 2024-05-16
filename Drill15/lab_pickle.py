import pickle

class Npc:
    def __init__(self, name, x, y):
        self.x, self.y, self.name = x, y, name

    # def __getstate__(self):
    #     state = {'x': self.x, 'y':self.y, 'name':self.name}
    #     return state
    #
    # def __setstate__(self, state):
    #     self.__dict__.update(state)

yuri = Npc('yuri', 100, 200)
jeni = Npc('jeni', 200, 400)
group = [yuri, jeni]

with open('npc.pickle', 'wb') as f:
    pickle.dump(group, f)

