
from collections import deque
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.root = data

    def insert(self, data):
        if self.root:
            if data < self.root:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.root:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.root = data

    # recursive
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.root, end=' ')
            self.inorder(root.right)

    def postOrder(self, root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.root, end=' ')

    def preOrder(self, root):
        if root:
            print(root.root, end=' ')
            self.preOrder(root.left)
            self.preOrder(root.right)

    # iterative method
    def iterativePreorder(self, root):
        stack = []
        while len(stack) != 0 or root is not None :
            if root is not None :
                print(root.root,end=' ')
                stack.append(root)
                # assign the new root
                root = root.left
            else:
                root = stack.pop()
                # assign the right child as the new root
                root = root.right

    def iterativeInorderTraversal(self, root):
        stack = []
        while len(stack) != 0 or root :

            if root :
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                print(root.root, end=' ')
                root = root . right

    # def iterativePostOrder(self,root):
    #     stack = []
    #     while len(stack) != 0 or root:
    #
    #         if root :
    #             stack.append(root)
    #             root = root.left
    #         else:
    #             temp = stack.pop()
    #             if temp > 0 :
    #                 stack.append(root)
    #                 root = int(root.left)
    #             else:
    #                 print(root.root,end=' ')
    #                 root = None

    def iterativePostOrderTraversal(self,root):
        if root is None:
            return

        stack1 , stack2 = [] , []
        stack1.append(root)
        while stack1:
            node = stack1.pop()
            stack2.append(node)

            if root.left:
                stack1.append(root.left)
            if root.right:
                stack1.append(root.right)
        while stack2:
            node = stack2.pop()
            print(node.root,end=' ')

    def levelOrderTraversal(self, root):
        # chech is root is None ot not
        if root is None:
            return  None
        res = []
        queue = []
        res.append(root.root)

        # add the root to the queue
        queue.append(root)
        while len(queue) != 0 :
            root = queue.pop(0)

            # chech if left subtree is empty or not
            if root.left :
                res.append(root.left.root)
                queue.append(root.left)
            if root.right :
                res.append(root.right.root)
                queue.append(root.right)
        return res

    def reverseLevelOrderTraversal(self,root):

        res , stack = [], []
        stack.append(root)
        while stack:
            node = stack.pop(0)
            if node is None:
                continue

            res.insert(0,node.root)
            if node.right:
                stack.append(node.right)
            if node.left :
                stack.append(node.left)
        return  res

# root = Node(5)
# for i in range(1, 12):
#     root.insert(i)
# root.inorder(root)
print()
# root.preOrder(root)
# print()
# root.postOrder(root)
# print()
# root.iterativePreorder(root)
# root.iterativeInorderTraversal(root)
# root.iterativePostOrderTraversal(root)

root = Node(10)
root.insert(20)
root.insert(30)
root.insert(40)
root.insert(60)


res = root.reverseLevelOrderTraversal(root)
print(res)
