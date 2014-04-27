import networkx as nx


class Railroad(nx.DiGraph):
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
