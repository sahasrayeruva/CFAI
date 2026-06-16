from typing import List

class ConstraintSolver:

    def __init__(self):
        # Simulated campus constraints
        self.constraints = {
            "Library": [],
            "Admin": [],
            "Lab": ["construction"],
            "Cafeteria": ["crowded"],
            "Classroom": [],
            "Auditorium": ["stairs"],
            "Parking": []
        }

    # --------------------------
    # Check if node satisfies constraints
    # --------------------------
    def is_valid(self, node, preferences):

        restrictions = self.constraints.get(node, [])

        for pref in preferences:
            if pref in restrictions:
                return False

        return True

    # --------------------------
    # Forward Checking
    # --------------------------
    def forward_check(self, path, preferences):

        for node in path:
            if not self.is_valid(node, preferences):
                return False

        return True

    # --------------------------
    # Explain why constraint failed
    # --------------------------
    def explain_failure(self, node, preferences):

        restrictions = self.constraints.get(node, [])

        for pref in preferences:
            if pref in restrictions:
                return f"{node} rejected because of {pref}."

        return "No constraint violation."

    # --------------------------
    # MRV Heuristic (Simplified)
    # --------------------------
    def mrv(self, available_nodes):

        return sorted(
            available_nodes,
            key=lambda x: len(self.constraints.get(x, []))
        )

    # --------------------------
    # Degree Heuristic (Simplified)
    # --------------------------
    def degree(self, graph):

        return sorted(
            graph.nodes(),
            key=lambda x: len(graph.neighbors(x)),
            reverse=True
        )

    # --------------------------
    # Least Constraining Value
    # --------------------------
    def lcv(self, neighbors):

        return sorted(neighbors)

    # --------------------------
    # Simple Backtracking Demo
    # --------------------------
    def backtracking(self, nodes, preferences):

        solution = []

        for node in nodes:

            if self.is_valid(node, preferences):
                solution.append(node)

        return solution