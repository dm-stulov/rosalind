''' 
        Author : Oguzhan Gencoglu - oguzhangencoglu90@gmail.com
 Creation Date : 03.08.2014
Latest Version : 03.08.2014

Solution of problem with the ID INI5 - Working with Files
in Rosalind.
'''

'''
Problem : INI5 - Working with Files

Given: A file containing at most 1000 lines.

Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
'''

# Import necessary modules
import numpy as np
from itertools import islice

if __name__ == "__main__":
    
    # Print problem name
    print "\nINI5 - Working with Files"
    
    # Run the algorithm
    
    
    with open("rosalind_ini5.txt") as fin, open('output.txt', 'w') as fout:
        fout.writelines(islice(fin, None, None, 2))
    
    '''
    text_file_read = open("rosalind_ini5.txt", "r")
    a =text_file_read.readline()

    s = text_file_read.readlines()
    text_file_read.close()
    
    text_file_write = open("Output.txt", "w")
    text_file_write.write(str(s[1::2]))
    text_file_write.close()'''