import pandas as pd

try:
    from .abs import Tree, TreeNode
except ImportError:
    from abs import Tree, TreeNode


class BinaryTree(Tree):

    def GetTreeView(self):
        frame = []
        for i in self.root:
            key = i.getKey()
            val = i.getVal()
            parent = i.getParent()
            left = i.getLeft()
            right = i.getRight()
            frame.append(
                [key, val, "left" if i.isLeft() else 'right' if not i.isRoot() else 'root', parent, left, right])

        return pd.DataFrame(frame, columns=['key', 'val', 'type', 'parent', 'left', 'right'])


if __name__ == '__main__':
    import random as rd
    tree = BinaryTree()

    td = [rd.randint(0, 9) for _ in range(10)]
    for i in td:
        tree[i] = i ** 2

    for i in tree:
        print(i)

    print(3 in tree)
    print(4 in tree)
    print(5 in tree)
