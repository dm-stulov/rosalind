''' 
        Author : Oguzhan Gencoglu - oguzhangencoglu90@gmail.com
 Creation Date : 03.08.2014
Latest Version : 03.08.2014

Solution of problem with the ID INI4 - Conditions and Loops
in Rosalind.
'''

'''
Problem : INI4 - Conditions and Loops

Given: Two positive integers a and b (a<b<10000).

Return: The sum of all odd integers from a through b, inclusively.
'''

# Import necessary modules
import numpy as np

if __name__ == "__main__":
    
    # Print problem name
    print "\nINI4 - Conditions and Loops"
    
    # Read the input from the text file and close the text file after reading
    text_file = open("rosalind_ini4.txt", "r")
    s = text_file.readlines()[0].strip()
    text_file.close()
    
    # Run the algorithm
    whitespace_index = s.find(" ")
    a = int(s[0:whitespace_index])
    b = int(s[whitespace_index::])
    
    if (a % 2 == 0):
        odd_sum = np.sum(np.arange(a + 1, b, 2))
    else:
        odd_sum = np.sum(np.arange(a, b, 2))

    # Display the result
    print "\nGiven the numbers", a, b
    print "\nResult is : ", odd_sum