''' 
        Author : Oguzhan Gencoglu - oguzhangencoglu90@gmail.com
 Creation Date : 24.07.2014
Latest Version : 24.07.2014

Solution of problem with the ID 1A - Frequent Words Problem in Rosalind.
'''

'''
Problem : 1A - Frequent Words Problem

Given: A DNA string s of length at most 1000 bp.

Return: Four integers (separated by spaces) representing the respective number
of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
'''

# Import necessary modules
import numpy as np

if __name__ == "__main__":
    
    # Print problem name
    print "\n1A - Frequent Words Problem"
    
    # Read the input from the text file and close the text file after reading
    text_file = open("rosalind_1a.txt", "r")
    [s, k] = text_file.readlines()[0:2]
    s = s.strip()
    k = int(k.strip())
    text_file.close()
    
    # Parse all kmers
    all_kmers = []
    for i in range(len(s)-k+1):
        all_kmers.append(s[i:i + k])
        
    unique_kmers = np.unique(all_kmers)
    
    # Count the occurences
    counts = []
    for kmer in unique_kmers:
        counts.append(all_kmers.count(kmer))
    
    # Get the most frequent k-mers
    counts = np.array(counts)
    inds = np.where(counts  == counts.max())[0]
    
    print "\nGiven the DNA string", s
    print "\nGiven k:", k
    print "\nMost common k-mers in the string are: ", unique_kmers[inds]
    
    