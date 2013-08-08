# 6.00x Problem Set 10
# Graph optimization
#
# A set of data structures to represent graphs
#

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    
    def getName(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    
    def getSource(self):
        return self.src
    
    def getDestination(self):
        return self.dest
    
    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)

class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}
    
    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    
    def childrenOf(self, node):
        return self.edges[node]
    
    def hasNode(self, node):
        return node in self.nodes
    
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]

# class WeightedEdge(Edge):
# 
#     def __init__(self, src, dest, total_distance, distance_outdoors):
#         super(WeightedEdge, self).__init__(src, dest)
#         self.total_distance = total_distance
#         self.distance_outdoors = distance_outdoors
#         self.weights = (self.total_distance, self.distance_outdoors)
#         
#     def getWeights(self):
#         return self.weights    
#     
#     def getTotalDistance(self):
#         return self.total_distance
#     
#     def getOutdoorDistance(self):
#         return self.distance_outdoors
#     
#     def __str__(self):
#         return '{0}->{1} ({2}, {3})'.format(self.src, self.dest, self.total_distance, self.distance_outdoors)
# 
# class WeightedDigraph(Digraph):
#     def __init__(self):
#         self.nodes = set([])
#         self.children = {}
#         self.edges = {}
#     
#     def addNode(self, node):
#         if node in self.nodes:
#             raise ValueError('Duplicate node')
#         else:
#             self.nodes.add(node)
#             self.children[node] = []
#     
#     def addEdge(self, edge):
#         src = edge.getSource()
#         dest = edge.getDestination()
#         weights = edge.getWeights()
#         if not(src in self.nodes and dest in self.nodes):
#             raise ValueError('Node not in graph')
#         self.children[src].append(dest)
#         self.edges[(src, dest)] = weights
#     
#     def childrenOf(self, node):
#         return self.children[node]
#     
#     def __str__(self):
#         res = ''
#         for k in self.edges:
#             #for d in self.edges[k]:
#             res = res + str(k) + ': ' + str(self.edges[k]) + '\n'
#         return res[:-1]

#     def addEdge(self, edge):
#         src = edge.getSource()
#         dest= edge.getDestination()
#         total_distance = edge.getTotalDistance()
#         outdoor_distance = edge.getOutdoorDistance()
#         if not (src in self.nodes and dest in self.nodes):
#             raise ValueError('Node not in graph')
#         self.edges[src].append(dest)
    
#     def __str__(self):
#         res = ''
#         for k in self.edges:
#             for d in self.edges[k]:
#                 res = '{0}{1}->{2} ({3}, {4})\n'.format(res, k, d, getTotalDistance(), getOutdoorDistance())
#         return res[:-1]
def floatify(tup):
    return str((float(tup[0]), float(tup[1])))
        


class WeightedDigraph(Digraph):
#     def addEdge(self, edge):
#         src = edge.getSource()
#         dest = edge.getDestination()
#         if not(src in self.nodes and dest in self.nodes):
#             raise ValueError('Node not in graph')
#         self.edges[src].append(edge)
    def __init__(self):
        self.nodes = set([])
        self.children = {}
        self.edges = {}
     
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.children[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        weights = edge.getWeights()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
#         if (src, dest) not in self.edges.keys():
#             raise ValueError('Node not in graph')
#         elif (src, dest) in self.edges.keys() and self.edges[(src, dest)] == weights:
#             raise ValueError('Node not in graph')
        self.children[src].append(dest)
        self.edges[(src, dest)] = weights
     
    def childrenOf(self, node):
        return self.children[node]

    def edgesFrom(self,node):
        '''Not implemented'''
        return [e for e in self.edges if e[0] == node]

    def __str__(self):
        res = ''
        for k,v in self.edges.iteritems():
            res = '{0}{1[0]}->{1[1]} {2}'.format(res, k, floatify(v)) + '\n'
        return res[:-1]

class WeightedEdge(Edge):
#     def __init__(self, src, dest, total_distance, outdoors_distance):
#         super(WeightedEdge, self).__init__(src, dest)
#         self.total_distance = total_distance
#         self.outdoors_distance = outdoors_distance
    
    def __init__(self, src, dest, total_distance, outdoor_distance):
        Edge.__init__(self, src, dest)
        self.total_distance = total_distance
        self.outdoor_distance = outdoor_distance
        self.weights = (total_distance, outdoor_distance)
    
    def getTotalDistance(self):
        return self.weights[0]
    
    def getOutdoorDistance(self):
        return self.weights[1]
    
    def getWeights(self):
        return self.weights 
        
    def __str__(self):
        return '{0}->{1} {2}'.format(self.src, self.dest, str(self.weights))
    
    
nx = Node('x')
ny = Node('y')
nz = Node('z')
e1 = WeightedEdge(nx, ny, 18, 8)
e2 = WeightedEdge(ny, nz, 20, 1)
e3 = WeightedEdge(nz, nx, 7, 6)
g = WeightedDigraph()
g.addNode(nx)
g.addNode(ny)
g.addNode(nz)
g.addEdge(e1)
g.addEdge(e2)
g.addEdge(e3)
print g

nj = Node('j')
nk = Node('k')
nm = Node('m')
ng = Node('g')
g = WeightedDigraph()
g.addNode(nj)
g.addNode(nk)
g.addNode(nm)
g.addNode(ng)
randomEdge = WeightedEdge(nm, ng, 13, 9)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(ng, nj, 19, 8)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nm, nk, 69, 30)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nk, ng, 81, 80)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nj, ng, 26, 9)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(ng, nk, 60, 13)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nk, nm, 52, 21)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nm, nk, 45, 31)
g.addEdge(randomEdge)
print g