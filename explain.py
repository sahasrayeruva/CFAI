"""
Explainable AI Module
CO6 - Explainable Artificial Intelligence
"""

from typing import List


class RouteExplainer:

    @staticmethod
    def generate_explanation(
        path: List[str],
        distance: float,
        algorithm: str,
        constraints=None,
        probability_info=None,
        utility_score=None
    ) -> str:

        explanation = []

        explanation.append(
            f"Route selected using {algorithm.upper()} algorithm."
        )

        explanation.append(
            f"Total distance: {distance:.2f} meters."
        )

        if constraints:
            explanation.append("\nConstraints Applied:")

            for c in constraints:
                explanation.append(f"✓ {c}")

        if probability_info:
            explanation.append(
                f"\nExpected delay probability: "
                f"{probability_info:.2f}"
            )

        if utility_score is not None:
            explanation.append(
                f"Utility Score: {utility_score:.2f}"
            )

        explanation.append("\nChosen Route:")

        for node in path:
            explanation.append(f"→ {node}")

        return "\n".join(explanation)