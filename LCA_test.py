import unittest
from LCA import Node, lca

def tree():
    root = Node(20) 
    root.left = Node(8) 
    root.right = Node(22) 
    root.left.left = Node(4) 
    root.left.right = Node(12) 
    root.left.right.left = Node(10) 
    root.left.right.right = Node(14) 

    return root

'''
Tree Generated:

          20
         /  \
        8   22
       / \          
      4  12
        /  \
       10  14
'''

root = tree()

class test_LCA(unittest.TestCase):
    def test_LCA_10_14(self):
        n1 = 10
        n2 = 14
        # lca(10, 14) ==> 12

        self.assertEqual(lca(root, n1, n2).data, 12)


    def test_LCA_14_8(self):
        n1 = 14
        n2 = 8
        # lca(14, 8) ==> 8

        self.assertEqual(lca(root, n1, n2).data, 8)


    def test_LCA_10_22(self):
        n1 = 10
        n2 = 22
        # lca(10, 22) ==> 20

        self.assertEqual(lca(root, n1, n2).data, 20)


    def test_LCA_4_12(self):
        n1 = 4
        n2 = 12
        # lca(4, 12) ==> 8

        self.assertEqual(lca(root, n1, n2).data, 8)


    def test_LCA_Empty(self):
        n1 = 0
        n2 = 0
        # lca(0, 0) ==> None

        self.assertEqual(lca(root, n1, n2), None)


    def test_LCA_NotPresent(self):
        n1 = 6123123
        n2 = 237875
        # lca(6123123, 237875) ==> None

        self.assertEqual(lca(root, n1, n2), None)


    def test_LCA_invalidtype(self):
        n1 = "not int"
        n2 = 100.609
        # lca("not int", 100.609) ==> None

        self.assertEqual(lca(root, n1, n2), None)


    def test_LCA_emptyroot(self):
        n1 = 4
        n2 = 12
        root = Node(0)
        # Root = 0
        # lca(4, 12) ==> None

        self.assertEqual(lca(root, n1, n2), None)


if __name__ == "__main__":
    unittest.main()