#coding=utf-8
import tree_builder
import tree_miner

routines = [    
           ['Cola','Egg','Ham'],
           ['Cola','Diaper','Beer'],
           ['Cola','Beer','Diaper','Ham'],
           ['Diaper','Beer']
        ]                                 # transaction datasets
min_sup = 2                             # the minimum support count
headerTable = {}        # head node table, used to store the index of each item

treeBuilder = tree_builder.Tree_builder(routines=routines, min_sup=min_sup, headerTable=headerTable)    # building FP_Tree
tree_miner.Tree_miner(Tree=treeBuilder.tree, min_sup=min_sup, headerTable=headerTable)         # mining frequent itemsets on FP_Tree