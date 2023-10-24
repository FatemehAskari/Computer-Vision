import networkx as nx
import matplotlib.pyplot as plt

# ساخت یک گراف دلخواه با ریشه 1
graph = nx.DiGraph()
graph.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (4, 9)])

# ساخت یک درخت با ریشه 1
tree = nx.dfs_tree(graph, 1)

# تعیین مختصات گره‌ها
pos = nx.nx_pydot.graphviz_layout(tree, prog='dot')

# رسم درخت
nx.draw(tree, pos, with_labels=True)

# نمایش نمودار
plt.show()