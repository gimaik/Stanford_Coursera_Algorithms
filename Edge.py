class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def weight(self):
        return self.weight

    def either(self):
        return self.v

    def other(self, vertex):
        if vertex == self.v:
            return self.w
        else:
            return self.v

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __eq__(self, other):
        return self.weight == other.weight
