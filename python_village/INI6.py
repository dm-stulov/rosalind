''' 
        Author : Oguzhan Gencoglu - oguzhangencoglu90@gmail.com
 Creation Date : 04.08.2014
Latest Version : 04.08.2014

Solution of problem with the ID INI6 - Dictionaries
in Rosalind.
'''

'''
Problem : INI6 - Dictionaries

Given: A string s of length at most 10000 letters.

Return: How many times any word occurred in string. Each letter case 
(upper or lower) in word matters. Lines in output can be in any order.
'''

# Import necessary modules
from scipy.stats import itemfreq

if __name__ == "__main__":
    
    # Print problem name
    print "\nINI6 - Dictionaries"
    
    # Read the input from the text file and close the text file after reading
    text_file = open("rosalind_ini6.txt", "r")
    s = text_file.readlines()[0].strip()
    text_file.close()
    
    # Get each word from the string
    words = []
    for word in s.split(' '):
        words.append(word)
        
    # Get the counts for each word
    dictionary = itemfreq(words)
    
    # Display the result
    for i in range(len(dictionary)):
        print dictionary[i,0], dictionary[i,1]