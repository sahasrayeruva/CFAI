import unittest

from graph import CampusGraph
from search import SearchAlgorithms


class TestNavigation(unittest.TestCase):

    def setUp(self):

        self.graph = CampusGraph("campus_map.json")

        self.search = SearchAlgorithms(
            self.graph
        )

    def test_bfs(self):

        result = self.search.bfs(
            "Lab",
            "Admin"
        )

        self.assertIsNotNone(result)
        self.assertIsNotNone(result.path)

    def test_dfs(self):

        result = self.search.dfs(
            "Lab",
            "Admin"
        )

        self.assertIsNotNone(result)
        self.assertIsNotNone(result.path)

    def test_ucs(self):

        result = self.search.ucs(
            "Lab",
            "Admin"
        )
        self.assertIsNotNone(result)
        self.assertGreater(result.cost, 0)

    def test_astar(self):

        result = self.search.astar(
            "Lab",
            "Admin"
        )
        self.assertIsNotNone(result)
        self.assertGreater(result.cost, 0)

    def test_same_source_destination(self):

        result = self.search.astar(
            "Lab",
            "Lab"
        )

        self.assertIsNotNone(result)
        self.assertEqual(result.path, ["Lab"])
        self.assertEqual(result.cost, 0)


if __name__ == "__main__":
    unittest.main()