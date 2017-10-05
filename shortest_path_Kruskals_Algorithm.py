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
    """This function will find the shortest path to
    connect all vertices in an undirected graph."""
    
    edges_sorted = sorted(Graph.edges, key=lambda edge:edge.value) # sort the edge by its value in ascending order
    
    connect_vertices = set() # create an empty set to add any vertice connected in minimum spanning tree
    adjacency_dict = {} # create an empty dictionary to add the adjacency list of any vertice included in the tree   
    
    while len(connect_vertices)<len(Graph.vertices):
        for edge in edges_sorted:
            if (edge.vertice1 not in connect_vertices) and (edge.vertice2 in connect_vertices):
                connect_vertices.add(edge.vertice1)   # connect not yet connected vertice1
                adjacency_dict[edge.vertice1.value] = []
                adjacency_dict[edge.vertice1.value].append((edge.value, edge.vertice2.value)) # add vertice 1 in connected vertices
                adjacency_dict[edge.vertice2.value].append((edge.value, edge.vertice1.value)) # update vertice 2 adjacency list
                edges_sorted.remove(edge)       # remove this edge from sorted edge list 
                break
            
            elif (edge.vertice1 in connect_vertices) and (edge.vertice2 not in connect_vertices):
                connect_vertices.add(edge.vertice2)   # connect not yet connected vertice 2
                adjacency_dict[edge.vertice2.value] = []
                adjacency_dict[edge.vertice2.value].append((edge.value, edge.vertice1.value)) # add vertice2 in connected nodes
                adjacency_dict[edge.vertice1.value].append((edge.value, edge.vertice2.value)) # update vertice 1 adjacency list
                edges_sorted.remove(edge)       # remove this edge from sorted edge list
                break
            
            elif (edge.vertice1 not in connect_vertices) and (edge.vertice2 not in connect_vertices):
                if len(connect_vertices) == 0:     # add vertice 1 and vertice 2 of the shortest edge and remove from edge list
                    connect_vertices.add(edge.vertice1)
                    adjacency_dict[edge.vertice1.value] = []
                    adjacency_dict[edge.vertice1.value].append((edge.value, edge.vertice2.value))
                    
                    connect_vertices.add(edge.vertice2)
                    adjacency_dict[edge.vertice2.value] = []
                    adjacency_dict[edge.vertice2.value].append((edge.value, edge.vertice1.value))
                    edges_sorted.remove(edge)
                    
                else:
                    continue
                
            else:
                continue
                
    return adjacency_dict