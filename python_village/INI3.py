''' 
        Author : Oguzhan Gencoglu - oguzhangencoglu90@gmail.com
 Creation Date : 03.08.2014
Latest Version : 03.08.2014

Solution of problem with the ID INI3 - Strings and Lists
in Rosalind.
'''

'''
Category: Python Village
Problem : INI3 - Strings and Lists

Given: A string s of length at most 200 letters and four integers a, b, c and d.

Return: The slice of this string from indices a through b and c through d (with 
space in between), inclusively.
'''

if __name__ == "__main__":
    
    # Print problem name
    print "\nINI3 - Strings and Lists"
    
    # Read the input from the text file and close the text file after reading
    text_file = open("rosalind_ini3.txt", "r")
    all_text = text_file.readlines()
    given_string = all_text[0].strip()
    ind_string = all_text[1].strip()
    text_file.close()
    
    # Run the algorithm
    ind = []
    ind_string = ind_string + " "
    for i in range(4):
        whitespace_index = ind_string.find(" ")
        ind.append(int(ind_string[0:whitespace_index]))
        ind_string = ind_string[whitespace_index + 1::]
    word1 = given_string[ind[0]:ind[1] + 1]
    word2 = given_string[ind[2]:ind[3] + 1]
        
    # Display the result
    print "\nGiven the string", given_string
    print "And indices", ind
    print "\nResult is : ", word1 + " " + word2