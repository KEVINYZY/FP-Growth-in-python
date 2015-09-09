#coding=utf-8
import tree_builder
import copy

class Tree_miner(object):
    """tree_miner class. 
    Function:mining frequent itemsets on FP-Tree."""
    def __init__(self, Tree=None, min_sup=-1, headerTable={}):
        """initialization for tree_miner class. Tree is the FP_Tree we are going to build, min_sup is the minimum support count, headerTable is the head node table of FP_Tree"""
        self.min_sup = min_sup
        self.tree_mining(Tree=Tree, headerTable=headerTable)
    
    
    def tree_mining(self, Tree, A=[], headerTable={}):
        """Function: mining the Frequent Itemsets recursively based on Tree. A is 'α' that in description document,and B is 'β'"""
        B = []
        allElem = {}        # it is used to save all nodes in the path when there is one single path.
        node = Tree.root       # node get the root of the tree
        while len(node.children) > 0:        # Judge whether a single path.
            if len(node.children) != 1:          # if the node in the path has not only one child,then it means the path is not a single path.
                break
            node = node.children.values()[0]        # node get the next node
            allElem.setdefault(node.data,node.count)        # recode the node in the path,it will be used if the path is a single path.
        if len(node.children) < 1:                  # Tree contains only a single path
            L = self.getL(items=allElem, min_sup=self.min_sup, A=A)     # L is the Frequent Itemsets we are working for.
            self.showResult(L)      # output the result
            return
        else:
            for item in headerTable:            # finding all the Frequent Itemsets ended with the element that in head node table.
                if A:                   
                    for elem in A:
                        if elem != []:
                            temp = copy.copy(elem)
                            B.append(temp)
                            B.append([item]+temp)
                else:
                    B.append([item])
                pattem,counts = self.findPattemBase(item, headerTable)      # get all the conditional pattern base that end with item. counts saves the count of the conditional pattern base.
                myHeaderTable = {}          
                conditionTree_builder = tree_builder.Tree_builder(routines=pattem, counts=counts, headerTable=myHeaderTable)        # new a Tree_builder object, used to build conditional FP-Tree.
                if conditionTree_builder.tree.root.children:            # if the conditional FP-Tree we built is not null
                    self.tree_mining(Tree=conditionTree_builder.tree, A=B, headerTable=myHeaderTable)       # recursive call
                B = []
        return
    
    
    def findPattemBase(self, item, headerTable):
        """Function:finding item's conditional pattern base base on the head node table of the tree."""
        itemPattem = []                 # save all the item's conditional pattern base
        counts = []                     # save the count of the conditional pattern base
        addressTable = headerTable[item]    # the address of all the node on item's list ,item is the element of head node table
        for itemNode in addressTable:           
            itemInPattem = []               # it is used to save the conditional pattern base of item
            nodeInPattem = itemNode.parent         # the element of the conditional pattern base,it can be used to roll back to the root,that is a pattern base
            if nodeInPattem.data == 'null':         # If its parent node is the root,then skip.
                continue
            while nodeInPattem.data != 'null':                  #If it's not to the root, then recall.
                itemInPattem.append(nodeInPattem.data)           
                nodeInPattem = nodeInPattem.parent          
            itemInPattem = tuple(itemInPattem)
            itemPattem.append(itemInPattem)             
            counts.append(itemNode.count)           # the count of the pattern base
        return itemPattem,counts
    
    
    def showResult(self, result=[[]]):
        """Function:showing the frequent itemsets we found"""
        for elem in result:
            num = elem.pop()        # the count of the frequent itemsets
            print tuple(elem),':',num
        return
    
    
    def combiner(self, myList, n): 
        """Function:get the permutation and combination of all the element in the list"""
        answers = []
        one = [0] * n 
        def next_c(li = 0, ni = 0): 
            if ni == n:
                answers.append(copy.copy(one))
                return
            for lj in xrange(li, len(myList)):
                one[ni] = myList[lj]
                next_c(lj + 1, ni + 1)
        next_c()
        return answers
    
    
    def findMinimum(self, items, elem):
        """Function:finding the minimun of the count of elem based on items(dictionary type)"""
        minimum = items[elem[0]]
        for a in elem:
            if items[a] < minimum:              # if the count of the element is smaller,then record the count.
                minimum = items[a]
        return minimum
    
    
    def getL(self, items, min_sup=-1, A=[]):
        """Function:for the tree who has only one path,get its frequent itemsets."""
        tempResult = []
        finnalResult = []
        nodes = items.keys()        # get the keys of items(dictionary type),those are all the nodes in the single-path.
        for i in range(1,len(nodes)+1):         # for the nodes,get their permutation and combination,those all the nodes in the path.
            tempResult += self.combiner(myList=nodes, n=i)
        for elem in tempResult[::-1]:           # traverse the tempResult reversely.it will be more expedient to delete the element.
            elemMinimum = self.findMinimum(items, elem)         # find the minimun count of elem
            if elemMinimum < min_sup:               # if the minimun is smaller the min_sup,then delete the elem
                tempResult.remove(elem)
            else:       # eles then put it into finnalResult.however,it is a conditional pattern base,so we need to add the last item to a frequent itemsets,and add the elemMinimun,too
                for Aelem in A:         
                    if Aelem:
                        temp = elem
                        temp += Aelem
                        temp.append(elemMinimum)
                        finnalResult.append(temp)               # save the frequent itemsets into finnalResult(list type)
        return finnalResult
    