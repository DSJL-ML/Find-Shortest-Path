# define Vertice, Edge, Graph class
class Vertice(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, vertice1, vertice2):
        self.value = value
        self.vertice1 = vertice1
        self.vertice2 = vertice2

class Graph(object):
    def __init__(self, vertices=[], edges=[], instance=None):
        self.vertices = vertices
        self.edges = edges
        self.instance = instance

    def insert_vertice(self, new_vertice_value):
        new_vertice = Vertice(new_vertice_value)
        self.vertices.append(new_vertice)
        
    def insert_edge(self, new_edge_value, vertice1_value, vertice2_value):
        vertice1_found = None
        vertice2_found = None
        for vertice in self.vertices:
            if vertice1_value == vertice.value:
                vertice1_found = vertice
            if vertice2_value == vertice.value:
                vertice2_found = vertice
        if vertice1_found == None:
            vertice1_found = Vertice(vertice1_value)
            self.vertices.append(vertice1_found)
        if vertice2_found == None:
            vertice2_found = Vertice(vertice2_value)
            self.vertices.append(vertice2_found)
        new_edge = Edge(new_edge_value, vertice1_found, vertice2_found)
        vertice1_found.edges.append(new_edge)
        vertice2_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        return [(i.value, i.vertice1.value, i.vertice2.value) for i in self.edges]

def shortest_path(Graph):
    minimum_travel = float("inf")
    for start in Graph.vertices: # initiate start vertice
        seen_list = [start] # vertices passed along on shortest path
        travel = 0
        adjacent_dict = {}
        while len(seen_list) < len(Graph.vertices):   # stop while loop when all the vertices being seen
            minimum_edge = float("inf")
            for edge in start.edges:
                if edge.value < minimum_edge:
                    if edge.vertice1 not in seen_list and edge.vertice2 in seen_list:
                        vertice_minimum = edge.vertice1
                        minimum_edge = edge.value
                    elif edge.vertice1 in seen_list and edge.vertice2 not in seen_list:
                        vertice_minimum = edge.vertice2
                        minimum_edge = edge.value
                    else:
                        pass
                else:
                    continue
                
            if vertice_minimum == start: # all the connection vertices from current vertice have been seen before
                start = previous      # go back to previous vertice
            else:
                if travel == 0:
                    adjacent_dict[start.value] = []
                    
                # add adjacent edge value and vertice value for previous vertice
                adjacent_dict[start.value].append((minimum_edge, vertice_minimum.value))
                previous = start   # assign previous vertice
                                                  
                seen_list.append(vertice_minimum) # add the vertice with the minimum edge
                start = seen_list[-1]   # reset start vertice to be the most recent seen vertice
                adjacent_dict[start.value] = []
                # add adjacent edge value and vertice value for the most recent seen vertice
                adjacent_dict[start.value].append((minimum_edge, previous.value))

            travel+=minimum_edge   # add up travel distance
            if travel <= minimum_travel:      # update minimum tree with shortest travel distance
                minimum_tree = adjacent_dict  
            else:
                pass

    return minimum_tree