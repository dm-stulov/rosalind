''' 
        Author : Oguzhan Gencoglu - oguzhangencoglu90@gmail.com
 Creation Date : 04.08.2014
Latest Version : 04.08.2014

Solution of problem with the ID INI5 - Working with Files
in Rosalind.
'''

'''
Category: Python Village
Problem : INI5 - Working with Files

Given: A file containing at most 1000 lines.

Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
'''

# Import necessary modules
from itertools import islice

if __name__ == "__main__":
    
    # Print problem name
    print "\nINI5 - Working with Files"
    
    # Run the algorithm - read every other line and write to an output file
    with open("rosalind_ini5.txt") as fin, open('output.txt', 'w') as fout:
        fout.writelines(islice(fin, 1, None, 2))