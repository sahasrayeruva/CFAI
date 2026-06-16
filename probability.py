import random


class ProbabilityEngine:

    def __init__(self):

        # Prior probabilities
        self.rain_probability = 0.30
        self.crowd_probability = {
            "Library": 0.40,
            "Admin": 0.20,
            "Lab": 0.15,
            "Cafeteria": 0.80,
            "Classroom": 0.30,
            "Auditorium": 0.50,
            "Parking": 0.10
        }

    # ----------------------------
    # Bayes Rule (Simplified)
    # ----------------------------
    def bayes(self, prior, likelihood, evidence):

        if evidence == 0:
            return 0

        return (likelihood * prior) / evidence

    # ----------------------------
    # Crowd Probability
    # ----------------------------
    def crowd_probability_of(self, node):

        return self.crowd_probability.get(node, 0.1)

    # ----------------------------
    # Expected Delay
    # ----------------------------
    def expected_delay(self, node):

        probability = self.crowd_probability_of(node)

        return probability * 10

    # ----------------------------
    # Sensor Fusion
    # ----------------------------
    def sensor_fusion(self, weather_sensor, crowd_sensor):

        return (weather_sensor + crowd_sensor) / 2

    # ----------------------------
    # Uncertainty Score
    # ----------------------------
    def uncertainty(self, node):

        return random.uniform(0.0, 1.0)

    # ----------------------------
    # Route Risk Score
    # ----------------------------
    def route_risk(self, path):

        risk = 0

        for node in path:
            risk += self.expected_delay(node)

        return round(risk, 2)

    # ----------------------------
    # Bayesian Recommendation
    # ----------------------------
    def recommend(self, path):

        risk = self.route_risk(path)

        if risk < 10:
            return "Low Risk Route"

        elif risk < 20:
            return "Moderate Risk Route"

        else:
            return "High Risk Route"