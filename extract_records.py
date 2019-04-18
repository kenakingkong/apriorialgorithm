'''
    program to extract records and export into csv
    which is fed into the apriori algorithm
'''

import csv
import re
import sys
import pandas as pd

def extract_stanzas():
    file_name = "dickinson_poems.txt"
    with open(file_name) as file:
        data = file.read()
    data = re.sub("(?:[A-Z ]+\.?\n\n){1,2}", '', data)
    stanzas = re.split("\n{2,}", data)
    return stanzas

def stanza_to_words(stanza):
    row = []
    stanza = re.sub("[^A-Za-z' \n]+", '', stanza.strip())
    for word in stanza.split():
        row.append(word.lower())
    return row


def main():
    stanzas = extract_stanzas()
    file = open('stanzas.csv', 'w')
    poet = csv.writer(file)
    for i in stanzas:
        poet.writerow(stanza_to_words(i))
    file.close()

if __name__ == "__main__":
    main()
