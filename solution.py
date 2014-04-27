import networkx as nx


class Railroad(nx.DiGraph):
    trips = []

    def populate_graph(self, graph_data):
        edges = [edge.strip() for edge in graph_data.split(',')]
        for edge in edges:
            left_node = edge[0]
            right_node = edge[1]
            weight = int(edge[2:])
            self.add_edge(left_node, right_node, weight=weight)

    def get_route_distance(self, route):
        route_edges = zip(route, route[1:])
        distance = 0
        for route_edge in route_edges:
            edge_data = self.get_edge_data(*route_edge)
            if edge_data is None:
                return "NO SUCH ROUTE"
            distance += edge_data['weight']
        return distance

    def set_trips(self, trips_data):
        self.trips = [trip.strip() for trip in trips_data.split(',')]

    def get_trips(self, start, end, max_stops=None):
        matching_trips = []
        for trip in self.trips:
            start_end_matches = trip.startswith(start) and trip.endswith(end)
            stops = len(zip(trip, trip[1:]))
            if (start_end_matches and max_stops is not None
                    and stops <= max_stops):
                matching_trips.append(trip)
            elif start_end_matches and max_stops is None:
                matching_trips.append(trip)
        return matching_trips
