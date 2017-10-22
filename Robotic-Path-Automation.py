from collections import defaultdict, deque
import matplotlib.pyplot as plt
from collections import OrderedDict
import numpy as np

class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)

if __name__ == '__main__':
    graph = Graph()

    for node in ['Source', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Destination']:
        graph.add_node(node)

    graph.add_edge('Source', 'A', 25.495)
    graph.add_edge('Source', 'B', 15.620)
    graph.add_edge('Source', 'C', 28.443)
    graph.add_edge('A', 'C', 30.480)
    graph.add_edge('A', 'E', 17.029)
    graph.add_edge('A', 'G', 25.495)
    graph.add_edge('A', 'H', 30.414)
    graph.add_edge('B', 'C', 16.763)
    graph.add_edge('B', 'E', 17.205)
    graph.add_edge('B', 'G', 40.050)
    graph.add_edge('C', 'E', 19.925)
    graph.add_edge('C', 'F', 50.695)
    graph.add_edge('D', 'E', 43.932)
    graph.add_edge('D', 'F', 13.5454)
    graph.add_edge('E', 'G', 28.636)
    graph.add_edge('E', 'H', 14.318)
    graph.add_edge('F', 'G', 70.007)
    graph.add_edge('F', 'H', 40.447)
    graph.add_edge('F', 'I', 39)
    graph.add_edge('F', 'J', 39)
    graph.add_edge('F', 'K', 77.078)
    graph.add_edge('G', 'I', 50.990)
    graph.add_edge('G', 'J', 80.622)
    graph.add_edge('G', 'K', 57.008)
    graph.add_edge('G', 'L', 74.330)
    graph.add_edge('H', 'I', 39.051)
    graph.add_edge('H', 'J', 62.650)
    graph.add_edge('H', 'K', 65.765)
    graph.add_edge('I', 'K', 38.079)
    graph.add_edge('I', 'L', 25)
    graph.add_edge('J', 'K', 57.009)
    graph.add_edge('J', 'L', 18.028)
    graph.add_edge('J', 'Destination', 41.231)
    graph.add_edge('K', 'Destination', 55.227)
    graph.add_edge('L', 'Destination', 32.016)
    print(shortest_path(graph, 'Source', 'Destination'))
x1, y1 = [5, 12], [25, 10]
x2, y2 = [28, 65], [5, 15]
x3, y3 = [22, 75], [24, 24]
x4, y4 = [10, 35], [50, 30]
x5, y5 = [60, 90], [60, 60]
x6, y6 = [45, 80], [95, 75]
plt.xlim(0, 120), plt.ylim(0, 120)
plt.xticks([10,20,30,40,50,60,70,80,90,100])
plt.yticks([10,20,30,40,50,60,70,80,90,100])
plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, linewidth=3.0, color="black", label="maze")
plt.plot([0], [0,],'ro', label="end points")
plt.plot([100], [100],'ro')
handles, labels = plt.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(),loc='upper left', frameon=False)
handles, labels = plt.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(),loc='upper left', frameon=False)
plt.annotate('A', xy=(5, 25), xytext=(4, 26))
plt.annotate('B', xy=(12, 10), xytext=(12, 6))
plt.annotate('C', xy=(28, 5), xytext=(25, 4))
plt.annotate('D', xy=(65, 15), xytext=(66, 14))
plt.annotate('E', xy=(22, 24), xytext=(18, 23))
plt.annotate('F', xy=(75, 24), xytext=(76, 23))
plt.annotate('G', xy=(10, 50), xytext=(7, 50))
plt.annotate('H', xy=(35, 30), xytext=(36, 28))
plt.annotate('I', xy=(60, 60), xytext=(57, 59))
plt.annotate('J', xy=(90, 60), xytext=(91, 60))
plt.annotate('K', xy=(45, 95), xytext=(42, 96))
plt.annotate('L', xy=(80, 75), xytext=(81, 72))
plt.annotate('Source', xy=(0, 0), xytext=(-4, -3))
plt.annotate('Destination', xy=(100, 100), xytext=(101, 101))

ax = plt.axes()
ax.arrow(0, 0, 11, 8.5, head_width=1.5, head_length=1.5, color='blue', label="path")
ax.arrow(22, 24, 12, 5, head_width=1.5, head_length=1.5, color='blue')
ax.arrow(12, 10, 9, 12.5, head_width=1.5, head_length=1.5, color='blue')
ax.arrow(35, 30, 24, 28, head_width=1.5, head_length=1.5, color='blue')
ax.arrow(60, 60, 19, 14, head_width=1.5, head_length=1.5, color='blue')
ax.arrow(80, 75, 18.5, 23.5, head_width=1.5, head_length=1.5, color='blue')

plt.show()
