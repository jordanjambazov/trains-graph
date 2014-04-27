import unittest
import solution


class TrainTests(unittest.TestCase):
    def setUp(self):
        self.railroad = solution.Railroad()
        graph_data = 'AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7'
        self.railroad.populate_graph(graph_data)
        trips_data = 'CDC, CEBC, CEBCDC, CDCEBC, CDEBC, CEBCEBC, CEBCEBCEBC'
        self.railroad.set_trips(trips_data)

    def test_railroad_graph_input(self):
        self.assertEqual(set(self.railroad.nodes()),
                         set(['A', 'B', 'C', 'D', 'E']),
                         'Railway stations do not match.')
        expected_edges = sorted([
            ('A', 'B', {'weight': 5}),
            ('B', 'C', {'weight': 4}),
            ('C', 'D', {'weight': 8}),
            ('D', 'C', {'weight': 8}),
            ('D', 'E', {'weight': 6}),
            ('A', 'D', {'weight': 5}),
            ('C', 'E', {'weight': 2}),
            ('E', 'B', {'weight': 3}),
            ('A', 'E', {'weight': 7}),
        ])
        edges = self.railroad.edges(data=True)
        self.assertEqual(sorted(edges), expected_edges,
                         'Distances between stations do not match.')

    def test_route_distance(self):
        distance_1 = self.railroad.get_route_distance('ABC')
        self.assertEqual(distance_1, 9, "Distance 1 does not match")

        distance_2 = self.railroad.get_route_distance('AD')
        self.assertEqual(distance_2, 5, "Distance 2 does not match")

        distance_3 = self.railroad.get_route_distance('ADC')
        self.assertEqual(distance_3, 13, "Distance 3 does not match")

        distance_4 = self.railroad.get_route_distance('AEBCD')
        self.assertEqual(distance_4, 22, "Distance 4 does not match")

        distance_5 = self.railroad.get_route_distance('AED')
        self.assertEqual(distance_5, "NO SUCH ROUTE",
                         "Wrong route does not match.")

    def test_trips(self):
        trips_from_c_to_c = self.railroad.get_trips('C', 'C', max_stops=3)
        self.assertEqual(len(trips_from_c_to_c), 2,
                         "Number of trips from C to C with 3 max stops.")

    def tearDown(self):
        del self.railroad


if __name__ == '__main__':
    unittest.main()
