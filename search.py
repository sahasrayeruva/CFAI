import heapq
import time
from collections import deque
from models import SearchResult


class SearchAlgorithms:

    def __init__(self, graph):
        self.graph = graph

    # -----------------------------
    # Reconstruct Path
    # -----------------------------
    def reconstruct_path(self, parent, goal):
        path = []

        while goal is not None:
            path.append(goal)
            goal = parent.get(goal)

        path.reverse()
        return path

    # -----------------------------
    # Path Cost
    # -----------------------------
    def path_cost(self, path):

        cost = 0

        for i in range(len(path) - 1):
            cost += self.graph.neighbors(path[i])[path[i + 1]]

        return cost

    # -----------------------------
    # Breadth First Search
    # -----------------------------
    def bfs(self, start, goal):

        start_time = time.time()

        queue = deque([start])

        visited = {start}

        parent = {start: None}

        expanded = 0

        while queue:

            current = queue.popleft()

            expanded += 1

            if current == goal:

                path = self.reconstruct_path(parent, goal)

                return SearchResult(
                    path,
                    self.path_cost(path),
                    expanded,
                    time.time() - start_time
                )

            for neighbor in self.graph.neighbors(current):

                if neighbor not in visited:

                    visited.add(neighbor)

                    parent[neighbor] = current

                    queue.append(neighbor)

        return None

    # -----------------------------
    # Depth First Search
    # -----------------------------
    def dfs(self, start, goal):

        start_time = time.time()

        stack = [start]

        visited = set()

        parent = {start: None}

        expanded = 0

        while stack:

            current = stack.pop()

            if current in visited:
                continue

            visited.add(current)

            expanded += 1

            if current == goal:

                path = self.reconstruct_path(parent, goal)

                return SearchResult(
                    path,
                    self.path_cost(path),
                    expanded,
                    time.time() - start_time
                )

            neighbors = list(self.graph.neighbors(current).keys())

            neighbors.reverse()

            for neighbor in neighbors:

                if neighbor not in visited:

                    parent[neighbor] = current

                    stack.append(neighbor)

        return None
    # -----------------------------
    # Uniform Cost Search (UCS)
    # -----------------------------
    def ucs(self, start, goal):

        start_time = time.time()

        priority_queue = []

        heapq.heappush(priority_queue, (0, start))

        parent = {start: None}

        cost_so_far = {start: 0}

        visited = set()

        expanded = 0

        while priority_queue:

            current_cost, current = heapq.heappop(priority_queue)

            if current in visited:
                continue

            visited.add(current)

            expanded += 1

            if current == goal:

                path = self.reconstruct_path(parent, goal)

                return SearchResult(
                    path,
                    current_cost,
                    expanded,
                    time.time() - start_time
                )

            for neighbor, edge_cost in self.graph.neighbors(current).items():

                new_cost = current_cost + edge_cost

                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:

                    cost_so_far[neighbor] = new_cost

                    parent[neighbor] = current

                    heapq.heappush(priority_queue, (new_cost, neighbor))

        return None
        # -----------------------------
    # Heuristic Function
    # -----------------------------
    def heuristic(self, node, goal):

        heuristic_values = {
            "Gate": 8,
            "Library": 6,
            "Admin": 5,
            "Lab": 3,
            "Cafeteria": 4,
            "Classroom": 2,
            "Auditorium": 2,
            "Parking": 0
        }

        return heuristic_values.get(node, 0)

    # -----------------------------
    # Greedy Best First Search
    # -----------------------------
    def greedy(self, start, goal):

        start_time = time.time()

        priority_queue = []

        heapq.heappush(
            priority_queue,
            (self.heuristic(start, goal), start)
        )

        parent = {start: None}

        visited = set()

        expanded = 0

        while priority_queue:

            _, current = heapq.heappop(priority_queue)

            if current in visited:
                continue

            visited.add(current)

            expanded += 1

            if current == goal:

                path = self.reconstruct_path(parent, goal)

                return SearchResult(
                    path,
                    self.path_cost(path),
                    expanded,
                    time.time() - start_time
                )

            for neighbor in self.graph.neighbors(current):

                if neighbor not in visited:

                    parent[neighbor] = current

                    heapq.heappush(
                        priority_queue,
                        (
                            self.heuristic(neighbor, goal),
                            neighbor
                        )
                    )

        return None
    
    # -----------------------------
    # A* Search Algorithm
    # -----------------------------
    def astar(self, start, goal):

        start_time = time.time()

        # Open list (priority queue)
        open_list = []

        heapq.heappush(
            open_list,
            (self.heuristic(start, goal), 0, start)
        )

        parent = {start: None}

        g_cost = {start: 0}

        closed_set = set()

        expanded = 0

        while open_list:

            f, current_g, current = heapq.heappop(open_list)

            if current in closed_set:
                continue

            closed_set.add(current)

            expanded += 1

            if current == goal:

                path = self.reconstruct_path(parent, goal)

                return SearchResult(
                    path,
                    g_cost[current],
                    expanded,
                    time.time() - start_time
                )

            for neighbor, edge_cost in self.graph.neighbors(current).items():

                tentative_g = g_cost[current] + edge_cost

                if neighbor not in g_cost or tentative_g < g_cost[neighbor]:

                    g_cost[neighbor] = tentative_g

                    parent[neighbor] = current

                    f_score = tentative_g + self.heuristic(neighbor, goal)

                    heapq.heappush(
                        open_list,
                        (
                            f_score,
                            tentative_g,
                            neighbor
                        )
                    )

        return None
    
    # -----------------------------
    # Run Selected Algorithm
    # -----------------------------
    def run(self, algorithm, start, goal):

        algorithm = algorithm.lower()

        if algorithm == "bfs":
            return self.bfs(start, goal)

        elif algorithm == "dfs":
            return self.dfs(start, goal)

        elif algorithm == "ucs":
            return self.ucs(start, goal)

        elif algorithm == "greedy":
            return self.greedy(start, goal)

        elif algorithm == "astar":
            return self.astar(start, goal)

        else:
            raise ValueError("Invalid Algorithm")