# CSE 101 - IP HW2
# K-Map Minimization 
# Name: Lakshya A Agrawal
# Roll Number:  2018242
# Section:  B
# Group: 3
# Date: 11 October 2018

def is_adjacent(num1, num2):
    '''
    Given 2 numbers(representing minterms), this function returns if they correspond to adjacet cells in k-map representation or not.
    return True if adjacent
    return False in all other cases
    '''
    n=abs(num1-num2)
    if (n==1) or (n==2) or (n==4) or (n==8):
        return(True)
    else:
        return(False)

def list_of_implicants_corresponding_minterm_given_size(size, minterm, func_as_list):
    lis=[]
    if func_as_list[minterm]==0:
        return(lis)
    else:
        if size==0:
            return(lis)
        elif size==1:
            lis.append([minterm])
            return(lis)
        elif size==2:
            i=0
            while i<len(func_as_list):
                if func_as_list[i]==1 and is_adjacent(minterm, i):
                    l=[minterm, i]
                    l.sort()
                    lis.append(l)
                else:
                    
                i=i+1

def list_of_implicants__full_function(numVar, func_as_list):
    '''
    This function takes a list represnting a given function as returned by the function function_rep_as_list() and returns a list, containing the prime implicants corresponding to each minterm in the function
    '''
    n=len(func_as_list)
    list_of_implicants=[]
    for i in range(0, n):
        l.append([])
    
    i=0
    while i<n:
        if func_as_list[i]==1:
            j=0
            while j<n:
                if func_as_list[j]==1 and is_adjacent(i,j):
                    

def function_rep_as_list(numVar, str1):
    '''
    Given the number of variables and string containing function representation, this function returns a list depicting the function, whose corresponfing elements correspond to the function minterms
    '''
    l=[]
    for i in range(0, 2**numVar):
        l.append(0)
    minterms, dont_care=str1.split()
    minterms=list(map(int, minterms[1:-1].split(',')))
    if not len(dont_care)==3:
        dont_care=list(map(int, dont_care[2:-1].split(',')))
    else:
        dont_care=[]
    for minterm in minterms:
        l[minterm]=1
    for dont in dont_care:
        l[dont]='X'
    return(l)

def minFunc(numVar, stringIn):
	"""
        This python function takes function of maximum of 4 variables
        as input and gives the corresponding minimized function(s)
        as the output (minimized using the K-Map methodology),
        considering the case of Don’t Care conditions.

	Input is a string of the format (a0,a1,a2, ...,an) d(d0,d1, ...,dm)
	Output is a string representing the simplified Boolean Expression in
	SOP form.

        No need for checking of invalid inputs.
        
	Do not include any print statements in the function.
	"""
	func_rep=function_rep_as_list(numVar, stringIn)
	stringOut=str(func_rep)
	return stringOut

print(minFunc(2, "(0) d(2)"))
