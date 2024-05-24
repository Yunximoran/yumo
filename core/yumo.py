import matplotlib.pyplot as plt
import networkx as nx


def draw_binary_tree(height):
    G = nx.Graph()

    # 添加节点
    for i in range(height):
        for j in range(2 ** i):
            G.add_node((i, j))

    # 添加边
    for i in range(1, height):
        for j in range(2 ** i):
            G.add_edge((i - 1, j // 2), (i, j))
            G.add_edge((i - 1, j // 2 + 1), (i, j + 1))

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=300, node_color=range(1, 2 ** height), font_size=12, font_weight="bold")

    plt.show()


draw_binary_tree(3)
