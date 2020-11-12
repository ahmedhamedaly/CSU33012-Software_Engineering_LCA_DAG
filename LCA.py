# Code adapted from geeksforgeeks.org

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def dagLCA(root, n1, n2):

    if root is None:
        return None

    if root.key == n1 or root.key == n2:
        return root

    if n1 == n2:
        return n1.key

    lca = []
    i = 0

    while(i < len(n1.pred)):
        j = 0
        while(j < len(n2.pred)):
            if(n1.pred[i].key == n2.pred[j].key):
                lca.append(n1.pred[i].key)
                j += 1
            else:
                j += 1
        i += 1

    if(lca == []):
        if(n1.key > n2.key):
            lca.append(dagLCA(root, n1.pred[0], n2))
        else:
            lca.append(dagLCA(root, n1, n2.pred[0]))

    return max(lca)


root = Node(1)
r2 = Node(2)
r3 = Node(3)
r4 = Node(4)
r5 = Node(5)
r6 = Node(6)
root.succ = [r2, r3, r4, r5]
r2.succ = [r4]
r2.pred = [root]
r3.succ = [r4, r5]
r3.pred = [root]
r4.succ = [r5]
r4.pred = [r2, r3, root]
r5.pred = [r3, r4, root]
r6.pred = [r4]
