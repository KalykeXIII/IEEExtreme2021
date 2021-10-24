# Task 4

from collections import defaultdict
from queue import Queue

class Graph:
    def __init__(self, no_cities):
        self.no_cities = no_cities
        self.graph = defaultdict(list)
        self.paths = []
        
    def add_edge(self, x, y):
        self.graph[x].append(y)
        
    def getPaths(self, source, dest, q):
        path = [source]
        q.put(path)
        
        while q.empty() == False:
            temp = q.get()
            last = temp[len(temp) - 1]
            if last == dest:
                return temp
            for link in self.graph[last]:
                if link not in temp:
                    new = temp + [link]
                    q.put(new)

# Get the number of cities
no_cities = int(float(input()))

# Create a list of cities to define the owners
owners = [0] * no_cities

# Set ownership
for i in range(no_cities):
    owners[i] = input().split(" ")
    
# Get paths
paths = owners[1:]

owners = owners[0]

# Number of events
no_events = int(float(input()))

# Get events
events = []

for i in range(no_events):
    events.append(input().split(" "))
    
        
# Create a city
city = Graph(no_cities)

# Create a queue
q = Queue()

# Add all paths the to city
for path in paths:
    city.add_edge(int(path[0]) - 1, int(path[1]) - 1)

print(city.getPaths(0, 0, q))
