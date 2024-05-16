import pickle


class Npc:
    def __init__(self, name, x, y):
        self.x, self.y, self.name = x, y, name

    # def __getstate__(self):
    #     state = {'x': self.x, 'y': self.y, 'name': self.name}
    #     return state
    #
    # def __setstate__(self, state):
    #     self.__dict__.update(state)

with open('npc.pickle', 'rb') as f:
    group = pickle.load(f)

for m in group:
    print(type(m))
    print(m.name, m.x, m.y)
print(group)