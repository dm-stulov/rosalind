''' 
        Author : Oguzhan Gencoglu - oguzhangencoglu90@gmail.com
 Creation Date : 23.07.2014
Latest Version : 23.07.2014

Solution of problem with the ID REVC - Complementing a Strand of DNA in 
Rosalind.
'''

'''
Problem : REVC - Complementing a Strand of DNA

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' 
and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing
the symbols of s, then taking the complement of each symbol (e.g., the reverse
complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
'''

if __name__ == "__main__":
    
    # Print problem name
    print "\nREVC - Complementing a Strand of DNA"
    
    # Read the input from the text file and close the text file after reading
    text_file = open("rosalind_revc.txt", "r")
    s = text_file.readlines()[0].strip()
    text_file.close()
    
    print "\nGiven the DNA string", s
    
    # Find the complement
    s = s.replace('A','t')
    s = s.replace('T','a')
    s = s.replace('G','c')
    s = s.replace('C','g')
    sc = s.upper()[::-1]
        
    # Display the result
    print "\nCorresponding reverse complementary DNA string is : ", sc