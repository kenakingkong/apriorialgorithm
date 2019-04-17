'''
    Apriori Algorithm
'''
import pandas as pd
import sys

class Candidate {
    constructor(){
        #this.parents =  []; not needed because of level?
        this.children = [];
        this.sup = 0;
        this.conf = 0;
        this.level = 0;
    }

    # returns true or false
    # checks all viable candidates in level before it to see if any are the parent
    def hasParents():
        pass;
}

def apriori(D,I,msup,mconf):

    # calculates the support for this level of candidates
    def compute_support(cTree, D):
        pass

    # calculates the confidence for this level of candidates
    def compute_confidence(cTree, D):
        pass

    # adds candidates as leaves from current node
    def extend_tree(cTree):

        pass

    #starting apriori function

    fTree = Candidate(); # result tree
    cTree = Candidate(); # prefix tree

    # add the first row of items
    for i in I:
        child = Candidate();
        child.level = 1;
        cTree.children.append(child)

    #
    while (c)

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
