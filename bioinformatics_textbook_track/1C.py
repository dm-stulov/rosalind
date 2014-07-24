''' 
        Author : Oguzhan Gencoglu - oguzhangencoglu90@gmail.com
 Creation Date : 24.07.2014
Latest Version : 24.07.2014

Solution of problem with the ID 1C - Pattern Matching Problem in Rosalind.
'''

'''
Problem : 1C - Pattern Matching Problem

Given: A DNA string s of length at most 1000 bp.

Return: Four integers (separated by spaces) representing the respective number
of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
'''

# Import necessary modules
import numpy as np

if __name__ == "__main__":
    
    # Print problem name
    print "\n1C - Pattern Matching Problem"
    
    # Read the input from the text file and close the text file after reading
    text_file = open("rosalind_1c.txt", "r")
    [s, k] = text_file.readlines()[0:2]
    pattern = s.strip()
    s = k.strip()
    text_file.close()
    
    # Parse all kmers
    all_kmers = []
    for i in range(len(s)-len(pattern)+1):
        all_kmers.append(s[i:i + len(pattern)])
    
    # Get the most frequent k-mers
    inds = np.where(np.array(all_kmers)  == pattern)[0]
    
    print "\nGiven the DNA string", s
    print "\nGiven the pattern:", pattern
    print "\nOccurence indices are: ", inds
    
    