# Given a node 'n' that represents a user on LinkedIn and value 'degree', return the number of connections in the degree 'n' for that user.
# Assume connections will be given as pairs [a, b] where a and b form an undirected component

class Degree:
    def __init__(self):
        self.val = -1
        

# Creates an adjacency list to represent the graph of the nodes passed in
def createGraph(nodes):
        
    graph = {}
    
    for node, neighbor in nodes:
        if node in graph:
            graph[node].append(neighbor)
        else:
            graph[node] = [neighbor]
    
    return graph

    

# Returns the degree between the nodes passed in. Returns -1 if nodes aren't connected
def getDegreeBetween(n1, n2, graph):
    
    degree = Degree() 
    visited = set()
    
    def recGetDegreeBetween(node1, node2, deg = 0):
        
        if node1 == node2:
            degree.val = deg
            return
        
        visited.add(node1)
        
        for neighbor in graph[node1]:
            if neighbor not in visited:
                recGetDegreeBetween(neighbor, node2, deg + 1)
    
    recGetDegreeBetween(n1, n2)
    return degree.val


# Returns all the nodes in the degree of node passed in
def getAllConnectionsInDegree(node, degree, graph):
    
    res = []
    visited = set()
    
    def recGetAllConnectionsInDegree(node, deg = 0):
        
        if deg == degree:
            res.append(node)
            return
        
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                recGetAllConnectionsInDegree(neighbor, deg + 1)
    
    recGetAllConnectionsInDegree(node)
    return res
    


# Testing
nodes = [["A","C"],
         ["A","D"],
         ["A","B"],
         ["A","E"],
         ["B","A"],
         ["B","F"],
         ["C","A"],
         ["C","M"],
         ["D","A"],
         ["E","A"],
         ["E","G"],
         ["F","B"],
         ["F","S"],
         ["G","E"],
         ["M","C"],
         ["S","F"],
         ["N","O"],
         ["O","N"]
         ]

graph = createGraph(nodes)
node1 = "B"
node2 = "G"
degree = 2

print("Connections for {} in degree {} -> {}".format(node1, degree, getAllConnectionsInDegree(node1, degree, graph)))

print("{} is in degree {} from {}".format(node1, getDegreeBetween(node1, node2, graph), node2))