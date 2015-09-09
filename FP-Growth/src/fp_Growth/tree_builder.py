#coding=utf-8
import tree_building

class Tree_builder(object):
    """tree_builder class。 
    Function:Prepare the data and structure the FP-Tree with the transaction datasets."""
    def __init__(self, routines, min_sup=-1, counts=[], headerTable={}):
        """initialization for class。 
        routines:the transaction datasets; min_sup:the minimum support count; counts:The number of times for each transaction,default is 1; headerTable:head node table,index table for each node on FP-Tree。"""
        self.routines = routines
        self.counts = counts
        self.min_sup = min_sup
        self.items = self.getItems(self.routines)          # get all the items
        self.sortedItems = self.getSortedItems(self.items)        # Sort all items, and remove the one smaller than min_sup.This result is Frequent 1-Itemsets.
        self.itemsTable = self.initItemsTable(headerTable)
        self.tree = self.treeBuilding(self.counts)
    
    
    def getItems(self, routines):
        """Function:scan the transaction datasets,return its itemsets and the count of each item."""
        items = {}
        for routine in routines:
            for elem in routine:
                    items.setdefault(elem,0)
                    items[elem] += 1
        return items
    
    
    def getSortedItems(self, items=None):
        """Function:sort the itemsets,and remove the non frequent item,get Frequent 1-Itemsets"""
        sortedItems = []
        temp = sorted(items.iteritems(), key=lambda asd:asd[1], reverse=True)       # sort items(dictionary type)
        for elem in temp:
            if elem[1] >= self.min_sup:             # Only take the items whose counts is greater than or equal to the minimum support count。
                sortedItems.append(elem[0])
        return sortedItems
    
    
    def getSortedRoutine(self, routine):
        """Function:sort one routine using the sorted Frequent 1-Itemsets."""
        sortedRoutine = []
        for elem in self.sortedItems:
            if elem in routine:
                sortedRoutine.append(elem)
        return sortedRoutine
    
    
    def initItemsTable(self, itemsTable):
        """Function:initialization for head node table."""
        for item in self.sortedItems:
            itemsTable.setdefault(item,[])
        return itemsTable
    
    
    def treeBuilding(self, counts):
        """Function:take out the routines one by one and build the FP-Tree."""
        tree = tree_building.Tree(itemTable=self.itemsTable)             # new a tree object
        for routine in self.routines:                           # take out the routines one by one
            sortedRoutine = self.getSortedRoutine(routine)          # sort the routine before using it to build the FP-Tree.
            if counts:                      # if the counts is not empty,it means that the tree was building with model base.And at this time,it needs to consider the count of model base.
                count = counts.pop(0)
            else:
                count =1
            tree.addRoutine(routine=sortedRoutine, Rroot=tree.root, count=count)             # build the tree with the sorted routine.
        return tree
    