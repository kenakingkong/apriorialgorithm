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

# calculates the RELATIVE support for this level of candidates
def compute_support(cTree, D):

    d_length = 0;
    c_length = len(cTree.children);

    # loop through children
    for c in range(0,c_length):
        data = cTree.children[c].x;
        count = 0;

        # get support xy
        for record in D:
            d_length +=1;   # saving length of D
            if data in record:
                count +=1

        # update rsup
        # rsup = sup(xy)/|d|
        cTree.children[c].sup = count / d_length;

    return cTree;

# calculates the RELATIVE confidence for this level of candidates
def compute_confidence(cTree, D):

    d_length = 0;
    c_length = len(cTree.children);

    # loop though children
    for c in range(0,c_length):
        data = cTree.children[c].x;
        count = 0;

        # get support xy
        for record in D:
            d_length +=1;
            if data in record:
                count +=1;

        # conf = sup(xy)/sup(x)
        confidence = count / cTree.children[c].sup

        # update with rconf
        # rconf = conf / |d| ??
        cTree.children[c].conf = confidence / d_length;

    return cTree;

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

    # trees are represented as a 2d list
    # each level is the next index
    fTree = []; # result tree
    cTree = []; # prefix tree

    # add the first row of items
    for i in I:
        child = Candidate();
        child.parent = cTree;
        child.level = 1;
        cTree.children.append(child)

    # loop through chidren
    while (len(cTree) > 0):

        # return cTree with updated min sup and confidence
        cTree = compute_support(cTree, D);
        cTree = compute_confidence(cTree, D);

        for child in cTree.children:
            if (child.sup >= minsup and child.conf >= minconf):
                # somehow add to F
                fTree.children.append(child);
            else:
                child.removed = True;

        # creates next level
        cTree = extend_tree(cTree);
        #cTree.level += 1;
        k +=1;

    return fTree;

# print association rule on each line
# x,y --> a,b,c
def print_rules(fTree, last_level):


    # get the parent
    # print the children (that aren't removed)

def main():

    if (len(sys.argv) != 3):
        print("Usage: python apriori <file.csv> minsup minconf");
        sys.exit();

    file = sys.argv[2];
    minsup = sys.argv[3];
    minconf = sys.argv[4];

    # convert file into database????? set of lists?

    # find the frequent sets
    freq_set = apriori(file, minsup, minconf);

    # print the association rules
    print_rules(freq_set);

if __name__ == "__main__":
    main()
