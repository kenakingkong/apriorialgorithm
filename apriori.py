'''
    Apriori Algorithm
'''
import pandas as pd
import sys

class Candidate {
    def __init__(self, x, parents, children, sup, conf, level, removed){
        self.x = "";
        self.parents =  [];
        self.children = [];
        self.sup = 0;
        self.conf = 0;
        self.level = 0;
        self.removed = False;
    }
}

# get the parents of current candidate
def get_parents(cTree):
    pass

# calculates the support for this level of candidates
def compute_support(cTree, D):
    pass

# calculates the confidence for this level of candidates
def compute_confidence(cTree, D):
    pass

# adds candidates as leaves from current node
def extend_tree(cTree):

    # get to the right level
    '''
    curr_children = cTree.children;
    while(len(curr_children) != 0 and
            curr_children[0].level != level):
        curr_children = cTree.children;
    '''
    curr_children = cTree.children;
    length = len(curr_children);
    for i in range(0,length):
        current = curr_children[i];
        for j in range(i,length):
            sibling = curr_children[j];
            child = Candidate();
            child.level = k+1;
            child.x =  set(current.x) | set(sibling.x);
            child.parents = get_parents(cTree, child.x);

            if (remove_child(child)):
                child.removed = True;
            current.children.append(child);

        if (len(current.childen) < 1):
            current.removed = True;

        return curr_children;


def apriori(D,I,msup,mconf):

    fTree = Candidate(); # result tree
    cTree = Candidate(); # prefix tree

    # add the first row of items
    for i in I:
        child = Candidate();
        child.parent = cTree;
        child.level = 1;
        cTree.children.append(child)

    # loop through chidren
    while (len(cTree) > 0):
        compute_support(cTree, D);
        for child in cTree.children:
            if (child.sup >= minsup):
                # somehow add to F
                fTree.children.append(child);
            else:
                child.removed = True;
        cTree = extend_tree(cTree);
        cTree.level += 1;
        k +=1;


def main():

    if (len(sys.argv) != 3):
        print("Usage: python apriori <file.csv> minsup minconf");
        sys.exit();

    file = sys.argv[2];
    minsup = sys.argv[3];
    minconf = sys.argv[4];

    # convert file into database????? set of lists?

    apriori(file, minsup, minconf);
    #association_rules = apriori(file, minsup, minconf);
    #print association_rules



if __name__ == "__main__":
    main()
