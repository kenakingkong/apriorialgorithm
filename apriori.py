'''
    Project 1: Apriori Algorithm
'''
import itertools
import sys

class Candidate:
    '''
    Returns a Candidate
    Similar to a tree node but tailored for the apriori algorithm
    '''
    def __init__(self, x=[], parents=[], children=[], sup=0, conf=0, level=0):
        self.x = x;
        self.parents =  parents;
        self.children = children;
        self.sup = sup;
        self.conf = conf;
        self.level = level;

    def __str__(self):
        return( "Candidate - level:" + str(self.level) + " s:" + str(self.sup) + " c:" + str(self.conf) +
                " data: " + ', '.join(str(x) for x in self.x))

    def __repr__(self):
        return( "Candidate - level:" + str(self.level) + " s:" + str(self.sup) + " c:" + str(self.conf) +
                " data:" + ''.join(str(x) for x in self.x))

    def __eq__(self, other):
        return (set(self.x) == set(other.x))

    def print_data(self):
        print(''.join(str(x) for x in self.x))

'''
    Helper Functions
'''

# pretty print a tree
def print_tree(tree):
    level = 0
    for node in tree:
        print("Level: %d" % level)
        for item in node:
            print(item)
        level+=1

# read csv file into 2d list representing Database
def read_csv(file):
    D = []
    with open(file) as f:
        for line in f:
            D.append(line.rstrip().split(","))
    return D

# wont work :(
# get all possible values
def get_unique(D):
    unique_list = set();
    for record in D:
        unique_list = unique_list | set(record)
    return list(unique_list)

# get all subsets of s of size k
def find_subsets(s, k):
    return [set(i) for i in itertools.combinations(s, k)]

# get all subsets (powerset?)
def find_powerset(s):
    s = list(s)
    x = len(s)
    powerset = []
    for i in range(1 << x):
        powerset.append(set(s[j] for j in range(x) if (i & (1 << j))))
    return powerset

'''
Apriori Functions
'''

# calculates the RELATIVE support for this level of candidates
def compute_support(c_level, k, D):

    d_length = 0;
    for record in D:
        d_length += 1;

        # generate subsets of length k
        subsets = find_subsets(set(record),k)

        for subset in subsets:
            for candidate in c_level:
                if subset.issubset(set(candidate.x)):
                    candidate.sup = round((candidate.sup) + (1/d_length),2);

    return c_level;

# adds candidates as leaves from current node
def extend_tree(tree, k):

    leaves = tree[k]
    length = len(leaves);
    tree.append([]);

    leaf_list = []
    for leaf in leaves:
        leaf_list.append(set(leaf.x))

    # for each leaf
    for a in range(0,length):
        leaf = leaves[a]

        # for each sibling leaf where b>a
        for b in range(a+1, length):
            sibling = leaves[b];

            data = set(leaf.x) | set(sibling.x)     # Xab = Xa U Xb
            #print(data)

            # prune candidates with infrequent subsets
            subsets = find_subsets(data, len(data)-1)
            #print(subsets)
            for subset in subsets:
                for leaf_set in leaf_list:
                    if (subset == leaf_set):
                        candidate = Candidate();
                        candidate.x = data;
                        candidate.level = leaf.level + 1
                        candidate.parents = leaf
                        #leaves[a].children.append(candidate);

                        # if acceptable, add leaf if not already added
                        if (candidate not in tree[k+1]):
                            tree[k+1].append(candidate);

        # if no extension
        if (len(leaves[a].children) == 0):
            leaves.pop(a);

    return tree;


# apriori algorithm
def apriori(D,I,minsup):

    fTree = [[Candidate()]]; # result
    cTree = [[Candidate()]]; # prefix tree

    # add initial single items
    k = 1;
    cTree.append([]);   #add level 1 to cTree
    for i in I:
        child = Candidate()
        child.x = [i];
        child.level = k;
        child.parents = [cTree[0][0]];
        cTree[0][0].children.append(child);
        cTree[k].append(child);

    # generate subsets until none left
    while (len(cTree[k])>0):

        cTree[k] = compute_support(cTree[k], k, D);

        # prune (add to F or remove from C[k])
        fTree.append([]);
        remove_list = []
        for leaf in cTree[k]:
            if (leaf.sup >= minsup):
                fTree[k].append(leaf)
            else:
                remove_list.append(leaf)

        for leaf in remove_list:
            cTree[k].remove(leaf);

        # generate candidates for frequent itemsets
        cTree = extend_tree(cTree, k);
        k +=1

    '''
    print("\nC: ")
    print_tree(cTree);
    print("\nF: ")
    print_tree(fTree);
    '''

    return fTree;


'''
    Rule Mining Functions
'''

# calculates the RELATIVE confidence
# support(I) - support(s)
def compute_confidence(I, s):
    return (I.sup - s.sup)

# prints the rules of the frequent itemsets
def print_rules(tree, minconf, d):

    for itemset in tree[1]:
        print(itemset.x)
        print(itemset.children)
        #for child in itemset.children:
    #        print(child.x)
        print("*")

        '''
        if (compute_confidence(itemset, child) >= minconf):
            x = ", ".join(itemset.x)
            y = ", ".join(child.x)
            print("%s --> %s" % (y,x))
        '''


    print("\nin the works");

# print all the frequent itemsets
def print_frequent_itemsets(tree):
    for level in tree:
        if not level[0].x :
            continue;
        for itemset in level:
            print("%s" % ", ".join(itemset.x))

def main():

    if (len(sys.argv) != 4):
        print("Usage: python apriori <file.csv> minsup minconf");
        sys.exit();

    file = sys.argv[1];
    minsup = float(sys.argv[2]);
    minconf = float(sys.argv[3]);

    # read file
    D = read_csv(file);
    I = get_unique(D);

    # find the frequent sets
    freq_set = apriori(D, I, minsup);
    #print("\n***F Tree***\n");
    #print_tree(freq_set)

    print("\n***Frequent Itemsets***\n")
    print_frequent_itemsets(freq_set)

    # print the association rules
    print("\n***Association Rules***\n")
    print_rules(freq_set, minconf, len(D));


if __name__ == "__main__":
    main()
