# CSE 101 - IP HW2
# K-Map Minimization 
# Name: Lakshya A Agrawal
# Roll Number:  2018242
# Section:  B
# Group: 3
# Date: 11 October 2018

def dec_to_bin(numVar, num):
    '''
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
    Given 2 numbers(representing minterms), this function returns if they correspond to adjacet cells in k-map representation or not.
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

'''
def list_of_adj_pos(numVar, minterm):
    if numVar==1:
        return([(minterm+1)%2])
    else:
        lis=[]
        i=0
        while i<2**numVar:
            if i==minterm:
                i=i+1
                continue
            else:
                if is_adjacent(numVar, i, minterm):
                    lis.append(i)
                i=i+1
        return(lis)
'''
def minterms_as_bin(numVar, function_rep_as_list):
    i=0
    lis=[]
    while i<len(function_rep_as_list):
        if function_rep_as_list[i]==1 or function_rep_as_list[i]=='X':
            lis.append(dec_to_bin(numVar, i))
        i=i+1
    return(lis)
    

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

def comm_expr(str1, str2, str_to_add):
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
	list_of_minterms_single=minterms_as_bin(numVar, func_rep)
	list_of_prime_implicants=func_list_of_prime_implicants(numVar, list_of_minterms_single, level=1)
	stringOut=str(list_of_prime_implicants)
	return stringOut

print(minFunc(4, "(0,1,2,4,5,12,13,8,9) d(5,14)"))
