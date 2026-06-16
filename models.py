from dataclasses import dataclass, field
from typing import Optional

@dataclass(order=True)
class PrioritizedNode:
    priority: float
    node: str = field(compare=False)
    cost: float = field(compare=False, default=0)
    parent: Optional[str] = field(compare=False, default=None)

@dataclass
class Agent:
    name: str
    source: str
    destination: str
    preference: str

@dataclass
class SearchResult:
    path: list
    cost: float
    expanded_nodes: int
    execution_time: float