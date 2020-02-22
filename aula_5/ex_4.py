
class Vetor:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self, vetor):
        self.x += vetor.x
        self.y += vetor.y

    def sub(self, vetor):
        pass

u = Vetor(1, 3)
v = Vetor(3, 5)

print(u.x) # 1
print(u.y) # 3

u.add(v)

print(u.x) # 4
print(u.y) # 8