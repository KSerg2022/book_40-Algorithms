
print('\n1 -- ')
import networkx as nx
G = nx.Graph()

G.add_node('Mike')
G.add_nodes_from(["Amine", "Wassim", "Nick"])

G.add_edge('Mike', 'Amine')
print('nodes - ', G.nodes)
print('edges - ', G.edges)

G.add_edge('Amine', 'Imran')
print('nodes - ', G.nodes)
print('edges - ', G.edges)



import matplotlib.pyplot as plt
nx.draw(G, with_labels=True, node_color='y', node_size=800)
plt.show()