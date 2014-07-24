# -*- coding: utf-8 -*-
''' 
        Author : Oguzhan Gencoglu - oguzhangencoglu90@gmail.com
 Creation Date : 24.07.2014
Latest Version : 24.07.2014

Solution of problem with the ID FIBO - Fibonacci Numbers in Rosalind.
'''

'''
Problem : FIBO - Fibonacci Numbers

Given: A positive integer n≤25.

Return: The value of Fn.
'''

# Define a function that gives the nth Fibonacci number
def fibo(n):
    fibo_list = [0, 1, 1]
    for i in range(n-1):
        fibo_list = fibo_list[-1:]+fibo_list[:-1]
        fibo_list[2] = fibo_list[0] + fibo_list[1]
    return fibo_list[2]
        
if __name__ == "__main__":
    
    # Print problem name
    print "\nFIBO - Fibonacci Numbers"
    
    # Read the input from the text file and close the text file after reading
    text_file = open("rosalind_fibo.txt", "r")
    n = text_file.readlines()[0].strip()
    text_file.close()
    
    # Display the result
    print "\n", n, "th fibonacci number is ", fibo(int(n))