class Graphe:

    def __init__(self, n):
        # self.adj = []
        # ligne = [0] * n
        # for i in range(n):
        #     self.adj.append(ligne)
        self.adj = [[0] * n for i in range(n)] 
    
    def ajoute_arc(self, s1, s2):
        self.adj[s1][s2] = 1
    
    def test_arc(self, s1, s2):
        # if self.adj[s1][s2] == 1:
        #     return True
        # else:
        #     return False
        return self.adj[s1][s2] == 1


G = Graphe(5)
print(G.adj)