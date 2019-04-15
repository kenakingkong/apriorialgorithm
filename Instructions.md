# Project 1
For this project we will learn find a data corpus and use Apriori algorithm to rule-mine it. 

You may work with one other individual on this project.

## Part 1) Find a corpus of data with the following characteristics

* This data must exist somewhere already, you cannot generate it. You will cite exactly where you got it from. Include a link in your report.
* There must be at least 1000 records (rows)
* Each record must contain at least 10 elements (basket items). There must not be significant repetition of exact records (more than 10).
* Write a program to parse and extract all records for analysis, and output to a CSV format, where each line contains a series of comma-separated strings. The lines do not have to have exactly the same number of items. Be careful that none of the items contains the comma character in it. Example:
milk, butter, apple, orange

butter, orange, nuclear bomb, carrot

...

## Part 2) Implement the Apriori algorithm

* Write a program called aprioi that takes exactly three command line arguments. Usage is: apriori CSV minsup minconf. CSV is the file name, minsup and minconf are the RELATIVE support and RELATIVE confidence (i.e. thy are both numbers between 0 and 1).
* You are submitting your own data, but your program must work with any valid CSV formatted data, not just your own CSV! Your program is responsib
* Your program must output a series of "rules" of the form "x,y --> a,b,c" where all the rules that meet minimum relative support and confidence are listed one line at a time.
CSV is the name of a local file such as your data set from part 1, in correct CSV format.
Your program must be able to compile and run on the CSC Unix machines. But there is no requirement to write it in any particular language.

## Part 3) Deliverables

* You MUST have a README file (without any extension, all caps and content in plain text) that has the names of you and your partner on the first line.
* README must also include a one paragraph description of data: what is it, and where does it come from? Link to the data.
* README must also include a paragraph about what you learned from this data.
README must also contain any instructions on how to make (compile) or any shortcomings and problems with your program.
* You must also submit the actual input CSV file, but no need to submit the data in the original format.
* Your source code and Makefile (if any)
* All your files, including README must be submitted together in tar.gz format. Do not make a directory. 
* Upload your files to Polylearn under this assignment.