import Tree.BinarySearchTree as BST

bst = BST.BST()

bst.add2(9)
bst.add2(3)
bst.add2(4)
bst.add2(8)
bst.add2(20)
bst.add2(11)
bst.add2(30)
bst.add2(12)
bst.add2(1)
bst.add2(0)
bst.add2(2)

def display_tree(bst: BST):
    for node in bst.breathFirst():
        print(node, end=' ')
    print('')

# print([str(node) for node in bst.breathFirst()])
visited, leaf_nodes = bst.depthFirst()
# print(
#     [str(node) for node in leaf_nodes]
# )

print(bst.height())