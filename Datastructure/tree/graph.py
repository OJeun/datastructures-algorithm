class Graph:
    def __init__(self):
        self.adj_list = {}

    # O(1)
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    # O(1)
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    # O(|E|)
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    # O(|V| + |E|)
    def remove_vertex(self, v1):
        if v1 in self.adj_list.keys():
            for other_vertex in self.adj_list[v1]:
                self.adj_list[other_vertex].remove(v1)
            del self.adj_list[v1]
            return True
        return False
                     