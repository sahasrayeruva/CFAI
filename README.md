# Intelligent Campus Navigation Assistant

## Overview

An AI-based campus navigation system that models a university campus as a graph and computes optimal routes using multiple search algorithms.

---

## Features

### CO1

- PEAS Agent
- Graph Representation
- State Space Search
- Dataclasses
- Logging
- Unit Testing

### CO2

Search Algorithms:

- BFS
- DFS
- UCS
- Greedy Best First Search
- A*

Performance comparison included.

### CO3

Constraint Satisfaction

- Avoid Construction
- Avoid Crowds
- Wheelchair Accessibility

### CO4

Utility-Based Decision Making

User priorities:

- Fastest Route
- Safest Route
- Balanced Route

### CO5

Bayesian Reasoning

Probability-based delay estimation:

- Rain Probability
- Crowd Probability
- Expected Delay

### CO6

Explainable AI

Generates human-readable reasoning:

- Why route was selected
- Constraints satisfied
- Utility score
- Delay probability

---

## Project Structure

```text
CampusNavigationAI/
│
├── main.py
├── graph.py
├── models.py
├── search.py
├── constraints.py
├── probability.py
├── utility.py
├── explain.py
├── profiling.py
├── logger.py
├── tests.py
├── campus_map.json
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run Application

```bash
python main.py
```

## Run Tests

```bash
python tests.py
```

## Algorithms Compared

| Algorithm | Optimal | Complete |
| ---------- | -------- | -------- |
| BFS | No | Yes |
| DFS | No | No |
| UCS | Yes | Yes |
| Greedy | No | Yes |
| A* | Yes | Yes |

## Future Enhancements

- Real-time GPS tracking
- Live crowd monitoring
- Dynamic rerouting
- Mobile App Integration

## Author

AI Mini Project
Intelligent Campus Navigation Assistant