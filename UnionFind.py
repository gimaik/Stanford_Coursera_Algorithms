class UnionFind:
    def __init__(self, N):
        self.count = N
        self.id = []
        for i in range(0, N+1):
            self.id.append(i)

    def count(self):
        return self.count

    def connected(self, p, q):
        return (self.find(p) == self.find(q))

    # def union(self, p, q):
    #     i = self.find(p)
    #     j = self.find(q)
    #
    #     if (i == j):
    #         return
    #
    #     self.id[i] = j
    #     self.count -= 1
    #
    # def find(self, p):
    #     while (p != self.id[p]):
    #         p = self.id[p]
    #     return p

    def union(self, p,q):

        pID = self.find(p)
        qID = self.find(q)

        if (pID == qID):
            return

        for i in range(0, len(self.id)):
            if self.id[i] == pID:
                self.id[i] = qID;
        self.count -= 1


    def find(self, p):
        return self.id[p]