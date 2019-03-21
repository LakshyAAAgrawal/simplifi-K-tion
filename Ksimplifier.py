# K-Map Minimization 
# Author : Lakshya A Agrawal
# Date: 16 October 2018

#import statements
import copy

def dec_to_bin(numVar, num):
    '''
    Input : numVar - Number of variables in boolean function/Number of digits required in decimal representation, num=Number to be represented in Binary
    Returns a string in given number of digits(numVar) representing num in binary
    '''
    i=0
    while True:
        t=2**i
        if t>num:
            i=i-1
            break
        i=i+1
    hext=''
    while i!=-1:
        z=num//(2**i)
        hext=hext+"01"[z]
        num=num-(2**i)*z
        i=i-1
    if hext=='':
        hext='0'
    if len(hext)!=numVar:
        hext='0'*(numVar-len(hext))+hext
    return(hext)

def is_adjacent(num1, num2):
    '''
    Input : 2 strings consisting of numVar number of characters, each either of ('0','1','X')
    
    Given 2 strings(representing minterms, or prime implicants), this function returns if they correspond to adjacet groups in k-map representation or not. Alternatively, this function returns if 2 implicants(rep by num1, num2) can be combined.
    
    return True if adjacent
    return False in all other cases
    '''
    i=0
    count=0
    while i<len(num1):
        if num1[i]!=num2[i]:
            if num1[i]=='-' or num2[i]=='-':
                return(False)
            if not (num1[i]=='-' or num2[i]=='-'):
                count=count+1
        i=i+1
        if count>=2:
            return(False)
    if count==1:
        return(True)
    else:
        return(False)

def minterms_as_bin(numVar, function_rep_as_list, match_against):
    '''
    Input : numVar = Number of varibales in boolean function, function_rep_as_list = A list consisting of 2^numVar elements, with each element corresponding to the functions value at that minterm(0, 1 or 'X' for dont care), match_against = the character to match against to form the list (0, 1, or 'X')
    
    Returns a list of minterms(as binary numbers) corresponding to matching terms
    '''
    i=0
    lis=[]
    while i<len(function_rep_as_list):
        if function_rep_as_list[i]==match_against:
            lis.append(dec_to_bin(numVar, i))
        i=i+1
    return(lis)
    

def function_rep_as_list(numVar, str1):
    '''
    Given the number of variables(numVar) and string containing function representation(str1), this function returns a list depicting the function, whose corresponfing elements correspond to the function minterms and have value(0,1 or 'X' for dont care)
    '''
    l=[]
    for i in range(0, 2**numVar):
        l.append(0)
    minterms, useless, dont_care=str1.split()
    if not len(minterms)==2:
        minterms=list(map(int, minterms[1:-1].split(',')))
    else:
        minterms=[]
    if not len(dont_care)==1:
        dont_care=list(map(int, dont_care[1:-1].split(',')))
    else:
        dont_care=[]
    for minterm in minterms:
        l[minterm]=1
    for dont in dont_care:
        l[dont]='X'
    return(l)

def comm_expr(str1, str2, str_to_add):
    '''
    Input : 2 strigs, str1 and str2, which correspond to binary representation of adjacent implicants in a k-map, i.e. is_adjacent() returns True. 
            str_to_add is the character to replace the 0 and 1 of the common variables with.
    
    Returns a string of same length as str1 and str2, which corresponds as an implicant to the implicants described by both of str1 and str2, with the combinable variable represented by the character in str_to_add
    '''
    i=0
    str_ret=''
    while i<len(str1):
        if str1[i]==str2[i]:
            str_ret=str_ret + str1[i]
        else:
            str_ret=str_ret + str_to_add
        i=i+1
    return(str_ret)

def func_list_of_prime_implicants(numVar, list_of_implicants, level=1):
    '''
    Input : numVar = number of variables in boolean function, list_of_implicants = This takes in a list of minterms to be combined(consisting of both, 1 and 'X', as Don't cares can be used to simplify)
    
    This is a recursive function which calls itself till the depth reaches the number of variables present in function. It iterates over each element in the current list_of_implicants and matches them against each other, checking if they can be combined. After all the possible terms have been combined, the function calls itself with the current list for the next iteration. This way, when the last depth level is reached, all the elements left in the list are only prime implicants. This acts as an auxiliary function for the function prime_implicants()
    
    Returns a list of prime implicants for the function, assuming all the elements in the original list are minterms.
    '''
    i=0
    lis_of_new_groups=[]
    while i<len(list_of_implicants):
        j=i
        while j<len(list_of_implicants):
            if is_adjacent(list_of_implicants[i], list_of_implicants[j]):
                lis_of_new_groups.append(comm_expr(list_of_implicants[i], list_of_implicants[j], '*'))
            j=j+1
        i=i+1
    for expr in lis_of_new_groups:
        a=expr.replace('*','1')
        if a in list_of_implicants:
            list_of_implicants.remove(a)
        a=expr.replace('*','0')
        if a in list_of_implicants:
            list_of_implicants.remove(a)
        a=expr.replace('*', '-')
        if not a in list_of_implicants:
            list_of_implicants.append(a)
    list_of_implicants.sort()
    if level+1>numVar:
        return(list_of_implicants)
    else:
        return(func_list_of_prime_implicants(numVar, list_of_implicants, level=level+1))

def prime_implicants(numVar, func_rep_as_list):
    '''
    Input : numVar = Number of varibales in boolean function, function_rep_as_list = A list consisting of 2^numVar elements, with each element corresponding to the functions value at that minterm(0, 1 or 'X' for dont care)
    
    This function returns a list of all prime implicants of the function whose representation is passed.
    It first calls the function func_list_of_prime_implicants with all minterms and dont cares. 
    Then it calls the same function with a list of Dont cares.
    Then, it removes all the prime implicants which cover only the don't cares, from the list of prime implicants to be returned.
    The final list thus obtained is a list of prime implicants only, for the given function.
    
    Returns a list of prime implicants corresponding to the given function, taking into account the presence of Don't cares.
    '''
    list_of_minterms_only_dont_care=minterms_as_bin(numVar, func_rep_as_list, 'X')
    list_of_minterms_incl_dont_care=minterms_as_bin(numVar, func_rep_as_list, 1) + list_of_minterms_only_dont_care
    list_of_minterms_incl_dont_care.sort()
    list_of_all_prime_implicants=func_list_of_prime_implicants(numVar, list_of_minterms_incl_dont_care, level=1)
    list_of_implicants_to_remove=func_list_of_prime_implicants(numVar, list_of_minterms_only_dont_care, level=1)
    for i in list_of_implicants_to_remove:
        if i in list_of_all_prime_implicants:
            list_of_all_prime_implicants.remove(i)
    return(list_of_all_prime_implicants)

def minterm_belong_to_prime(minterm, prime_implicant):
    '''
    Input : minterm = A string representing a minterm in binary form, prime_implicant = A string representing a prime_implicant in the form '01--' where '-' represents the combined variables.
    
    Returns True if the minterm is covered  by the prime implicant
    Returns False in all other cases
    '''
    i=0
    while i<len(prime_implicant):
        if prime_implicant[i]=='-':
            i=i+1
            continue
        else:
            if prime_implicant[i]!=minterm[i]:
                return(False)
        i=i+1
    return(True)

def prime_implicants_by_minterms(numVar, list_of_prime_implicants, func_rep_as_list):
    '''
    Input : numVar = Number of varibales in boolean function, list_of_prime_implicants = a list of all the prime implicants which cover the minterms in the function(as obtained from the function prime_implicants()),function_rep_as_list = A list consisting of 2^numVar elements, with each element corresponding to the functions value at that minterm(0, 1 or 'X' for dont care)
    
    Returns a list of lists, with each element being a list of prime implicants, which cover the minterm present at the same index in the list - list_of_minterms as obtained from minterms_as_bin
    '''
    list_of_minterms=minterms_as_bin(numVar, func_rep_as_list, 1)
    list_of_prime_implicant_by_minterm=[]
    i=0
    while i<len(list_of_minterms):
        a=[]
        j=0
        while j<len(list_of_prime_implicants):
            if minterm_belong_to_prime(list_of_minterms[i], list_of_prime_implicants[j]):
               a.append(list_of_prime_implicants[j])
            j=j+1
        list_of_prime_implicant_by_minterm.append(a)
        i=i+1
    return(list_of_prime_implicant_by_minterm)
                
def list_of_all_possible_solutions(lis_of_prime_implicant, prime_imp_by_minterms, list_of_sol, level=0, solution=[]):
    '''
    Input : lis_of_prime_implicant = A list of prime implicants of the function to be minimized(as obtained from prime_implicants)
            prime_imp_by_minterms = A list of lists, with each element being a list of prime implicants, which cover the minterm present at the same index in the list - list_of_minterms as obtained from minterms_as_bin (as obtained from prime_implicants_by_minterms)
            list_of_sol = The list to which the list of possible solutions should be appended. It should be an empty list for all practical purposes.
            Others are for internal use.
    
    This function generates a list of lists, with each element(list) representing a possible solution for the given function. For this, it recursively generates a list of all prime_implicants that must be included to cover all the minterms. All the solutions are appended to the list supplied under list_of_sol
    '''
    if level==0:
        for i in prime_imp_by_minterms[level]:
            a=[]
            a.append(lis_of_prime_implicant.index(i))
            list_of_all_possible_solutions(lis_of_prime_implicant, prime_imp_by_minterms, list_of_sol, level=level+1, solution=a)
    elif 0<level<len(prime_imp_by_minterms):
        for i in prime_imp_by_minterms[level]:
            c=copy.deepcopy(solution)
            if not lis_of_prime_implicant.index(i) in c:
                c.append(lis_of_prime_implicant.index(i))
            list_of_all_possible_solutions(lis_of_prime_implicant, prime_imp_by_minterms, list_of_sol, level=level+1, solution=c) 
    else:
        solution.sort()
        if not solution in list_of_sol:
            list_of_sol.append(solution)
def reduce_to_min_number_of_implicants(list_of_all_solutions):
    '''
    Input : list_of_all_solutions = a list of lists, with each element(list) representing a possible solution for the given function(as obtained from                                                                   list_of_all_possible_solutions())
    
    This function first compares the number of terms required by each solution in the list_of_all_solutions, and then finds the smallest number of terms required.
    It then returns a list of lists(representing solutions) which contains the smallest number of terms in the soltion possible.
    '''
    smallest=10000000
    for i in list_of_all_solutions:
        if len(i)<smallest:
            smallest=len(i)
    final=[]
    for i in list_of_all_solutions:
        if len(i)==smallest:
            final.append(i)
    return(final)

def solution_as_string(list_of_prime_implicant, solution):
    '''
    Input : list_of_all_prime_implicant = list of prime implicants covering the functions(as obtained from prime_implicants), solution = A list consisting of indices corresponding to prime implicants in the list_of_prime_implicants.
    
    Returns a list of strings, with each string containing one term of the function SOP, example - "wx'y" 
    '''
    list_of_terms=[]
    for i in solution:
        a=list_of_prime_implicant[i]
        j=0
        str_to_add=''
        while j<len(a):
            if a[j]=='-':
                None
            elif a[j]=='0':
                str_to_add=str_to_add+['w','x','y','z', 'a', 'b', 'c'][j]+'\''
            else:
                str_to_add=str_to_add+['w','x','y','z', 'a', 'b', 'c'][j]
            j=j+1
        list_of_terms.append(str_to_add)
    return(list_of_terms)

def number_of_literals(list_of_prime_implicants, solution):
    '''
    Input : list_of_all_prime_implicant = list of prime implicants covering the functions(as obtained from prime_implicants), solution = A list consisting of indices corresponding to prime implicants in the list_of_prime_implicants.
    
    Returns the number of different literals present in the given solution. For this purpose, "w" and "w'" are treated as separate literals.
    '''
    literal=[]
    for i in solution:
        a=list_of_prime_implicants[i]
        j=0
        str_to_add=''
        while j<len(a):
            if a[j]=='-':
                None
            elif a[j]=='0':
                lite=['w','x','y','z','a', 'b', 'c'][j]+'\''
                if not lite in literal:
                    literal.append(lite)
            else:
                lite=['w','x','y','z', 'a', 'b', 'c'][j]
                if not lite in literal:
                    literal.append(lite)
            j=j+1
    return(len(literal))
        
def red_based_on_number_of_literals(list_of_prime_implicant, lis_of_solutions):
    '''
    Input : list_of_all_prime_implicant = list of prime implicants covering the functions(as obtained from prime_implicants), lis_of_solutions = a list of lists, with each element(list) representing a possible solution for the given function(as obtained after reducing by the number of terms by the function reduce_to_min_number_of_implicants)
    
    This function first checks the number of literals used in each solution and finds the smallest number of literals used in any solution. It then makes a list of all solutions containing the smallest number of literals.
    
    Returns a list of lists, with each element representing a solution after being reduced for based on number of literals.
    '''
    smallest=10000000
    red_list=[]
    for i in lis_of_solutions:
        z=number_of_literals(list_of_prime_implicant, i)
        if z<smallest:
            smallest=z
    for i in lis_of_solutions:
        if number_of_literals(list_of_prime_implicant, i)==smallest:
            red_list.append(i)
    return(red_list)

def minFunc(numVar, stringIn):
	func_rep=function_rep_as_list(numVar, stringIn)
	list_of_prime_implicants=prime_implicants(numVar, func_rep)
	if len(list_of_prime_implicants)==0:
	     return('0')
	lis_of_prime_implicant_by_minterm=prime_implicants_by_minterms(numVar, list_of_prime_implicants, func_rep)
	list_of_solutions=[]
	list_of_all_possible_solutions(list_of_prime_implicants, lis_of_prime_implicant_by_minterm, list_of_solutions)
	reduced_list_of_all_possible_solutions_by_number_of_minterms=reduce_to_min_number_of_implicants(list_of_solutions)
	red_list_based_on_number_of_literals=red_based_on_number_of_literals(list_of_prime_implicants, reduced_list_of_all_possible_solutions_by_number_of_minterms)
	final_solution=red_list_based_on_number_of_literals[0]
	if list_of_prime_implicants[final_solution[0]]==('-'*numVar):
	     return('1')
	
	final_solution=[]
	for i in red_list_based_on_number_of_literals:
	     final_solution.append('+'.join(sorted(solution_as_string(list_of_prime_implicants, i))))
	return ' OR '.join(sorted(final_solution))
