# -*- coding: utf-8 -*-
''' 
        Author : Oguzhan Gencoglu - oguzhangencoglu90@gmail.com
 Creation Date : 04.08.2014
Latest Version : 04.08.2014

Solution of problem with the ID FIBD - Mortal Fibonacci Rabbits
in Rosalind.
'''

'''
Category: Bioinformatics Stronghold
Problem : FIBD - Mortal Fibonacci Rabbits

Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence 
Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed 
that each pair of rabbits reaches maturity in one month and produces a single 
pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic 
programming solution in the case that all rabbits die out after a fixed number
of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live
for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th 
month if all rabbits live for m months.
'''

if __name__ == "__main__":
    
    # Print problem name
    print "\nFIBD - Mortal Fibonacci Rabbits"
    
    # Read the input from the text file and close the text file after reading
    text_file = open("rosalind_fibd.txt", "r")
    s = text_file.readlines()[0].strip()
    text_file.close()
    
    # Run the algorithm
    whitespace_index = s.find(" ")
    n = int(s[0:whitespace_index])
    k = int(s[whitespace_index::])

    fib = [1]*k
    for i in range(k - 2):
        fib.append(fib[-2] + fib[-1])
    for j in range(n - k):
            fib.append(fib[-2] + fib[-1] - fib[-k-1])
        
    # Display the result
    print "\nGiven the numbers", n, k
    print "\nResult is : ", fib[-1]