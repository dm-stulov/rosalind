''' 
        Author : Oguzhan Gencoglu - oguzhangencoglu90@gmail.com
 Creation Date : 23.07.2014
Latest Version : 23.07.2014

Solution of problem with the ID DNA - Counting DNA Nucleotides in Rosalind.
'''

'''
Category: Bioinformatics Stronghold
Problem : DNA - Counting DNA Nucleotides

A string is simply an ordered collection of symbols selected from some alphabet
and formed into a word; the length of a string is the number of symbols that it
contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A',
'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of
times that the symbols 'A', 'C', 'G', and 'T' occur in s.
'''

# Import necessary modules
import numpy as np

if __name__ == "__main__":
    
    # Print problem name
    print "\nDNA - Counting DNA Nucleotides"
    
    # Read the input from the text file and close the text file after reading
    text_file = open("rosalind_dna.txt", "r")
    s = text_file.readlines()[0].strip()
    text_file.close()
    
    # Get the alphabet
    alphabet = np.unique(s)
    
    # Count the occurences
    counts = []
    for symbol in alphabet:
        counts.append(s.count(symbol))
        
    # Display the result
    print "\nGiven the DNA string", s
    print "\nNucleotide counts are : ", counts
    
    