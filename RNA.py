''' 
        Author : Oguzhan Gencoglu - oguzhangencoglu90@gmail.com
 Creation Date : 23.07.2014
Latest Version : 23.07.2014

Solution of problem with the ID RNA - Transcribing DNA into RNA in Rosalind.
'''

'''
Problem : RNA - Transcribing DNA into RNA

An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', 
and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA
string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
'''

if __name__ == "__main__":
    
    # Read the input from the text file and close the text file after reading
    text_file = open("rosalind_rna.txt", "r")
    t = text_file.readlines()[0].strip()
    text_file.close()
    
    t = list(t)
    for i in range(len(t)):
        if (t[i] == 'T'):
            t[i] = 'U'
    t = ''.join(t)
        
        
    # Display the result
    print "The result of RNA - Transcribing DNA into RNA is : ", t