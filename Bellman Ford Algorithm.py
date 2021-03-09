#This is the implementation of the bellman ford algorithm using python 3.9.1
#This algorithm is used to solve the shortest path problem with O(V*E) running time complexity 
#it can be used in FOREX market to detect negative cycles
#the 09/03/21

class Edge:

    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight 
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

class Node:

    def __init(self, name):
        self.name = name
        self.adjacency_list = []
        self.predecessor = None
        self.min_distance = float('int')


class BellmanFord:

    def __init__(self, vertex_list, start_vertex, edge_list):
        self.vertex_list = vertex_list
        self.start_vertex = start_vertex
        self.edge_list = edge_list
        self.has_cycle = False

    def find_shortest_path(self):

        self.start_vertex.min_distance = 0

        for i in range(len(self.vertex_list) - 1):
            for edge in self.Edge_list:
                u = Edge.start_vertex
                v = Edge.start_vertex

                dist = u.min_distance + Edge.weight

                if  dist < min.distance :
                    v.predecessor = u
                    v.min_distance = dist

        for edge in self.edge_list:
            if self.check_cycle(edge):
                print("Neagtive cycle detected ....")
                return 

    def check_cycle(self):
        if Edge.start_vertex.min_distance + Edge.weight < Edge.target_vertex.min_distance:
            self.has_cycle = True
            return True
        else:
            return False

    def get_shortest_path(self, vertex):

        if not self.has_cycle:
            print("Shortest path exist with value:", vertex.min_distance)
            node = vertex
            while node is not None:
                print(node.name)
                node = node.predecessor
        else:
            print("There's no negative cycle in this graph")


