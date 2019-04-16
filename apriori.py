'''
    Apriori Algorithm
'''
import pandas as pd
import sys

def apriori(D,msup,mconf):
    #inner functions so that f and c are global

    # calculates the support for this level of candidates
    def compute_support(ctree, D):
        pass

    # adds candidates as leaves from current node
    def extend_tree(ctree):
        pass

    # rest of the code here i think

            # create F (result tree)
            # create C (prefix tree)

    pass

def main():

    if (len(sys.argv) != 3):
        print("Usage: python apriori <file.csv> minsup minconf");
        sys.exit();

    file = sys.argv[2];
    minsup = sys.argv[3];
    minconf = sys.argv[4];

    # turn file into database???
    # apriori(D,minsup,minconf);
    apriori(file, minsup, minconf);


if __name__ == "__main__":
    main()
