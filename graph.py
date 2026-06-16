import json

class CampusGraph:

    def __init__(self, filename):
        with open(filename, "r") as f:
            self.graph = json.load(f)

    def neighbors(self, node):
        return self.graph[node]

    def nodes(self):
        return list(self.graph.keys())