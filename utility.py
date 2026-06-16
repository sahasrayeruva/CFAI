class UtilityEngine:

    def __init__(self):
        pass

    # ---------------------------------
    # Utility Function
    # ---------------------------------
    def utility(self, distance, risk, preference):

        if preference == "fastest":
            return -(distance)

        elif preference == "safest":
            return -(risk)

        elif preference == "balanced":
            return -(distance + risk)

        else:
            return -(distance + risk)

    # ---------------------------------
    # Choose Best Route
    # ---------------------------------
    def choose_best(self, routes, preference):

        best_route = None
        best_score = float("-inf")

        for route in routes:

            score = self.utility(
                route["distance"],
                route["risk"],
                preference
            )

            if score > best_score:

                best_score = score
                best_route = route

        return best_route

    # ---------------------------------
    # Policy Selection
    # ---------------------------------
    def policy(self, preference):

        policies = {
            "fastest": "Shortest Distance Policy",
            "safest": "Minimum Risk Policy",
            "balanced": "Balanced Utility Policy"
        }

        return policies.get(preference, "Balanced Utility Policy")

    # ---------------------------------
    # Bounded Rationality
    # ---------------------------------
    def bounded_rationality(self, routes):

        # Instead of checking every route,
        # only consider first 3 routes.

        return routes[:3]

    # ---------------------------------
    # Minimax (Simplified Demo)
    # ---------------------------------
    def minimax(self, values):

        return min(values)

    # ---------------------------------
    # Alpha-Beta Pruning Concept
    # ---------------------------------
    def alpha_beta(self, values):

        alpha = float("-inf")
        beta = float("inf")

        best = None

        for value in values:

            alpha = max(alpha, value)

            if alpha >= beta:
                break

            best = alpha

        return best

    # ---------------------------------
    # Expectimax Concept
    # ---------------------------------
    def expectimax(self, values):

        if len(values) == 0:
            return 0

        return sum(values) / len(values)

    # ---------------------------------
    # Multi-Agent Reasoning
    # ---------------------------------
    def multi_agent(self, pedestrian_delay, vehicle_delay):

        return (pedestrian_delay + vehicle_delay) / 2