class Node:
    def __init__(self, item):
        self.nome = item
        self.prox = None
    def __str__(self):
        return self.nome