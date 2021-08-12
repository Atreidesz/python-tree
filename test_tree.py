import unittest

from Tree import Tree as Tree

class Test_Tree(unittest.TestCase):
    def setUp(self):
        self.root = Tree(0)
        self.node_1   = Tree(1,   self.root)
        self.node_3   = Tree(3,   self.root)
        self.node_2   = Tree(2,   self.root)
        self.node_13  = Tree(13,  self.node_1)
        self.node_11  = Tree(11,  self.node_1)
        self.node_12  = Tree(12,  self.node_1)
        self.node_122 = Tree(122, self.node_12)
        self.node_121 = Tree(121, self.node_12)
        self.node_21  = Tree(21,  self.node_2)
        self.node_22  = Tree(22,  self.node_2)
        self.node_23  = Tree(23,  self.node_2)
        self.node_211 = Tree(211, self.node_21)

    # Constructor tests
    def test_01_root_children(self):
        root_children = self.root.children
        self.assertEqual(len(root_children), 3)
        self.assertEqual(root_children[0], self.node_1)
        self.assertEqual(root_children[1], self.node_2)
        self.assertEqual(root_children[2], self.node_3)

    def test_02_node_2_children(self):
        node_2_children = self.node_2.children
        self.assertEqual(len(node_2_children), 3)
        self.assertEqual(node_2_children[0], self.node_21)
        self.assertEqual(node_2_children[1], self.node_22)
        self.assertEqual(node_2_children[2], self.node_23)

    # Walk
    def test_10_walk_root(self):
        nodelist = self.root.walk()
        idlist = [item.id for item in nodelist]
        self.assertEqual(idlist, [0,1,11,12,121,122,13,2,21,211,22,23,3])

    def test_11_walk_id_root(self):
        nodeidlist = self.root.walk_id()
        self.assertEqual(nodeidlist, [0,1,11,12,121,122,13,2,21,211,22,23,3])

    def test_12_walk_node_2(self):
        nodeidlist = self.node_2.walk_id()
        self.assertEqual(nodeidlist, [2,21,211,22,23])

    # Detach, attach
    def test_20_detach(self):
        self.node_2.detach()
        nodeidlist = self.root.walk_id()
        self.assertEqual(nodeidlist, [0,1,11,12,121,122,13,3])

    def test_21_attach(self):
        # Move node_2 under node_3
        self.node_2.attach(self.node_3)
        nodeidlist = self.root.walk_id()
        self.assertEqual(nodeidlist, [0,1,11,12,121,122,13,3,2,21,211,22,23])

    def test_22_attach_without_detach(self):
        # Move back to original location
        self.node_2.attach(self.root)
        nodeidlist = self.root.walk_id()
        self.assertEqual(nodeidlist, [0,1,11,12,121,122,13,2,21,211,22,23,3])

    def test_30_duplicate_child(self):
        with self.assertRaises(ValueError):
            self.node_2_dup = Tree(2, self.root)


if __name__ == '__main__':
    unittest.main()
