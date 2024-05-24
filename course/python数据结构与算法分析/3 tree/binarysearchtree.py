# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.parent = None  # 父节点
#         self.left = None
#         self.right = None
#
#     def hasLeft(self):
#         return self.left
#
#     def hasRight(self):
#         return self.right
#
#     def isLeft(self):
#         return True if self.parent and self.parent.left == self else False
#
#     def isRight(self):
#         return True if self.parent and self.parent.right == self else False
#
#     def isRoot(self):
#         return True if not self.parent else False
#
#     def isLeaf(self):
#         return True if self.left is None or self.right is None else False
#
#     # 布尔表达式取值
#     def hasAnyChild(self):  # 左右子节点存在任意一个
#
#         """
#         # 或运算
#         right = a
#         left = b
#
#         if a is true
#             return a
#         else:
#             if b is true
#                 reutrn b
#             else:
#                 return a
#         :return:
#         """
#         return self.right or self.left
#
#     def hasBothChild(self):  # 左右子节点是否都存在
#         return self.right and self.left
#
#
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#         self.size = 0
#
#     def length(self):
#         return self.size
#
#     def __len__(self):
#         return self.size
#
#     def __iter__(self):
#         return self.root.__iter__()
#
#
# if __name__ == '__main__':
#     pass
