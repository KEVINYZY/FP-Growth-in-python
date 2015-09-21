#FP-Growth coded with python2.7#
FP-Growth is one of the most classical algorithms in the association analysis.And this repository is one implementation of the FP-Growth with python language.
<br>
<br>
##Contents:##
* FP_Growth
  * \__init__.py 
  * tree_builder.py 
  * tree_building.py 
  * tree_miner.py
<br>
"\__init__.py":This file is calling the other files to build the FP-Tree and to mine frequent itemsets on FP_Tree.And also,we are inputting transaction datasets and setting the minimum support count here.
<br>
"tree_builder.py":This file is responsible for processing the transaction datasets and calling "tree_building.py" to build the FP_Tree.
<br>
"tree_building.py":This file is responsible for building the FP_Tree.
<br>
"tree_miner.py":This file is used to mine the frequent itemsets based on the FP_Tree.

<br>
<br>
##Result:##
if the transaction datasets and min_sup that we input in "\__init__.py" like this:
```
......
routines = [    
           ['Cola','Egg','Ham'],
           ['Cola','Diaper','Beer'],
           ['Cola','Beer','Diaper','Ham'],
           ['Diaper','Beer']
        ]                                 # transaction datasets
min_sup = 2                             # the minimum support count
......
```
<br>
then,the result will be:
```
('Diaper', 'Beer') : 3
('Cola', 'Ham') : 2
('Beer', 'Diaper', 'Cola') : 2
('Diaper', 'Cola') : 2
('Beer', 'Cola') : 2

```

<br>
<br>
#####You can see more Chinese explanation here:http://blog.csdn.net/bone_ace/article/details/46746727
