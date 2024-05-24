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
                [key, val, parent, left, right, "left" if i.isLeft() else 'right' if not i.isRoot() else 'root'])

        return pd.DataFrame(frame, columns=['key', 'val', 'parent', 'left', 'right', 'type'])


if __name__ == '__main__':
    td = [3, 1, 7, 4, 9, 5, 2, 6, 8, 0]
    tree = BinaryTree()
    for d in td:
        tree[d] = d * 2

    print(tree.GetTreeView())
    print(len(tree))
