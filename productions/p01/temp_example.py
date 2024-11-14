# TODO to be removed

import networkx as nx
import matplotlib.pyplot as plt

# Define the graph and add edges with weights
G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'D', weight=2)
G.add_edge('A', 'C', weight=3)
G.add_edge('C', 'D', weight=4)

# Define the positions for each node
pos = nx.spring_layout(G)  # You can use spring_layout for a nice spread

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15, font_weight='bold', edge_color='gray')

# Draw edge labels with weights
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

# Highlight the shortest path
shortest_path = nx.shortest_path(G, 'A', 'D', weight='weight')
path_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

# Display the graph
plt.title('Graph with Shortest Path Highlighted')
plt.show()
