''' 
        Author : Oguzhan Gencoglu - oguzhangencoglu90@gmail.com
 Creation Date : 03.08.2014
Latest Version : 03.08.2014

Solution of problem with the ID INI2 - Variables and Some Arithmetic
in Rosalind.
'''

'''
Problem : INI2 - Variables and Some Arithmetic

Given: Two positive integers a and b, each less than 1000.

Return: The integer corresponding to the square of the hypotenuse of the right 
triangle whose legs have lengths a and b.
'''

if __name__ == "__main__":
    
    # Print problem name
    print "\nINI2 - Variables and Some Arithmetic"
    
    # Read the input from the text file and close the text file after reading
    text_file = open("rosalind_ini2.txt", "r")
    s = text_file.readlines()[0].strip()
    text_file.close()
    
    # Run the algorithm
    whitespace_index = s.find(" ")
    a = int(s[0:whitespace_index])
    b = int(s[whitespace_index::])
    
    # Display the result
    print "\nGiven the numbers", a, b
    print "\nResult is : ", (a**2 + b**2)