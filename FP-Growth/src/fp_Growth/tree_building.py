#coding=utf-8

class Node(object):
    """Node class.
    Function:new a tree node."""
    def __init__(self, data=-1, count=0, parent=None):
        """initialization for Node class.A node information includes: its value, count, father node, all its child nodes"""
        self.data = data
        self.count = count
        self.parent = parent
        self.children = {}
    
    
class Tree(object):
    """tree_growth class.
    Function:building tree"""
    def __init__(self, data=-1, parent=None, itemTable=None):
        """initialization for tree_growth class,and new a tree root"""
        self.root = Node(data='null', parent=self)
        self.itemTable = itemTable
    
    
    def addRoutine(self, routine, Rroot, count):
        """Function:build the tree recursively based on routine. Rroot is the root of the tree, count is number of the routine(it would be used on building the condition FP-Tree)"""
        if len(routine) <= 0:       # if the length of routine is zero,then return.
            return
        elem = routine.pop(0)
        if elem in Rroot.children:          # if the element of routine is already in the tree's existing path.
            nextNode = Rroot.children[elem]           
        else:                                       # else:new a path
            newNode = Node(data=elem, parent=Rroot)         # new a tree node
            Rroot.children.setdefault(elem,newNode)         # Put the new node in the children's list of the current node.
            nextNode = newNode
        nextNode.count += count         # update the count of the node in the path.
        if nextNode not in self.itemTable[elem]:        # if the next node is new,then put it into the head node table.
            self.itemTable[elem].append(nextNode)
        self.addRoutine(routine=routine, Rroot=nextNode, count=count)           # build the tree recursively
        return
    