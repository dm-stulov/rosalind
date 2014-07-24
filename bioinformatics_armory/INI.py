''' 
        Author : Oguzhan Gencoglu - oguzhangencoglu90@gmail.com
 Creation Date : 24.07.2014
Latest Version : 24.07.2014

Solution of problem with the ID INI - Introduction to the Bioinformatics Armory
in Rosalind.
'''

'''
Problem : INI - Introduction to the Bioinformatics Armory

Given: A DNA string s of length at most 1000 bp.

Return: Four integers (separated by spaces) representing the respective number
of times that the symbols 'A', 'C', 'G', and 'T' occur in s. Note: You must
provide your answer in the format shown in the sample output below.
'''

# Import necessary modules
import numpy as np

if __name__ == "__main__":
    
    # Print problem name
    print "\nINI - Introduction to the Bioinformatics Armory"
    
    # Read the input from the text file and close the text file after reading
    text_file = open("rosalind_ini.txt", "r")
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