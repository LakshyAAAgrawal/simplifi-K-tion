# K-Map Minimization 
# Test File
# Author : Lakshya A Agrawal
# Date: 16 October 2018

import unittest
from Ksimplifier import minFunc
from Ksimplifier import dec_to_bin
from Ksimplifier import function_rep_as_list
from Ksimplifier import comm_expr
from Ksimplifier import is_adjacent
from Ksimplifier import func_list_of_prime_implicants
from Ksimplifier import prime_implicants
from Ksimplifier import minterm_belong_to_prime
from Ksimplifier import prime_implicants_by_minterms
from Ksimplifier import number_of_literals

class testpoint(unittest.TestCase):
    def test_dec_to_bin(self):
        '''
        Test the function to generate binary representation of a number in given number of digits.
        '''
        self.assertEqual(dec_to_bin(1,1),'1')
        self.assertEqual(dec_to_bin(2,2),'10')
        self.assertEqual(dec_to_bin(3,5),'101')
        self.assertEqual(dec_to_bin(4,15),'1111')
        self.assertEqual(dec_to_bin(4,10),'1010')
    
    def test_function_rep_as_list(self):
        '''
        Tests the function used to parse user input for processing by the function minFunc
        '''
        self.assertEqual(function_rep_as_list(1,'(0) d -'), [1,0])
        self.assertEqual(function_rep_as_list(2,'(2) d (1)'), [0,'X',1,0])
        self.assertEqual(function_rep_as_list(3,'(5,3) d (7)'), [0,0,0,1,0,1,0,'X'])
        self.assertEqual(function_rep_as_list(4,'(1,7,3,14) d (2,6)'), [0,1,'X',1,0,0,'X',1,0,0,0,0,0,0,1,0])
        self.assertEqual(function_rep_as_list(3,'(0,2,4) d (7)'), [1,0,1,0,1,0,0,'X'])
    
    def test_comm_expr(self):
        '''
        Tests the function to generate a common expression for 2 given implicants which are adjacent to each other
        '''
        self.assertEqual(comm_expr('0010', '0000', '-'),'00-0')
        self.assertEqual(comm_expr('001-', '000-', '*'),'00*-')
        self.assertEqual(comm_expr('001', '000', '-'),'00-')
        self.assertEqual(comm_expr('--1-', '--0-', '-'),'----')
        self.assertEqual(comm_expr('1-', '0-', '-'),'--')
        self.assertEqual(comm_expr('01', '00', '-'),'0-')
        self.assertEqual(comm_expr('1', '0', '-'),'-')
    
    def test_is_adjacent(self):
        '''
        Tests the function which checks whether 2 given implicants are adjacent(can be combined) or not
        '''
        self.assertEqual(is_adjacent('000','010'), True)
        self.assertEqual(is_adjacent('--0','--1'), True)
        self.assertEqual(is_adjacent('-0-','-01'), False)
        self.assertEqual(is_adjacent('0','1'), True)
        self.assertEqual(is_adjacent('011','111'), True)
        self.assertEqual(is_adjacent('-1-','-0-'), True)
        self.assertEqual(is_adjacent('-1-','-01'), False)
        self.assertEqual(is_adjacent('0','1'), True)
        self.assertEqual(is_adjacent('00-0','0-01'), False)
    
    def test_minterm_belong_to_prime(self):
        self.assertEqual(minterm_belong_to_prime('0000','00--'), True)
        self.assertEqual(minterm_belong_to_prime('0110', '01-0'), True)
        self.assertEqual(minterm_belong_to_prime('0101', '1---'), False)
        self.assertEqual(minterm_belong_to_prime('001', '-1-'), False)
        self.assertEqual(minterm_belong_to_prime('01', '-1'), True)
    
    def test_prime_implicants_by_minterms(self):
        self.assertEqual(prime_implicants_by_minterms(4, ['-1-0', '-11-', '0-01', '01--', '1-10'],[0,'X',0,0,1,1,1,'X',0,'X',1,0,'X',0,1,'X']), [['-1-0','01--'],['0-01','01--'],['-1-0', '-11-', '01--'],['1-10'],['-1-0', '-11-', '1-10']])
        self.assertEqual(prime_implicants_by_minterms(4,['-001', '-010', '-100', '-111', '0-10', '01-0', '011-', '1-0-', '10-0', '11-1'],[0,'X','X',0,'X',0,1,1,1,1,1,0,1,'X',0,1]),[['0-10','01-0','011-'],['-111','011-'],['1-0-','10-0'],['-001','1-0-'],['-010','10-0'],['-100','1-0-'],['-111', '11-1']])
        
    def test_func_list_of_prime_implicants(self):
        self.assertEqual(func_list_of_prime_implicants(4,['0000','0001','0010','0100','0101','1000','1001','1100','1101','1110']),['--0-','00-0','11-0'])
        self.assertEqual(func_list_of_prime_implicants(4,['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']),['----'])
        self.assertEqual(func_list_of_prime_implicants(4,['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110']),['---0','--0-','-0--','0---'])
        self.assertEqual(func_list_of_prime_implicants(4,['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110']),['---0','--0-','-0--','0---'])
        self.assertEqual(func_list_of_prime_implicants(3,['000','001','010','011','100','101','110','111']),['---'])
        self.assertEqual(func_list_of_prime_implicants(3,['011','101','110']),['011','101','110'])
        self.assertEqual(func_list_of_prime_implicants(2,['00','01','10','11']),['--'])
    
    def test_number_of_literals(self):
        self.assertEqual(number_of_literals(['--00', '--11', '-0-1', '-00-', '-1-0', '-11-', '1--1', '1-0-', '11--'], [2, 1, 0, 8]), 7)
    
    def test_prime_implicants(self):
        self.assertEqual(prime_implicants(4,[0,0,0,0,0,'X',0,'X',0,0,'X',0,0,'X',0,0]),[])
        self.assertEqual(prime_implicants(4,[1,1,1,0,1,'X',0,0,1,1,0,0,1,1,'X',0]),['--0-','00-0','11-0'])
        self.assertEqual(prime_implicants(4,[1,0,'X','X',0,'X',0,0,0,0,0,0,0,'X',1,'X']),['00-0','111-'])
        self.assertEqual(prime_implicants(4,[1,0,0,0,'X',0,0,'X',1,'X','X',0,1,0,1,0]),['--00','1--0','100-'])
        self.assertEqual(prime_implicants(3,['X','X','X',1,'X',0,'X',1]),['-1-','0--'])
        self.assertEqual(prime_implicants(3,['X','X',0,0,0,0,'X',1]),['11-'])
        self.assertEqual(prime_implicants(3,[1,0,'X',1,'X',0,1,0]),['--0','01-'])
        self.assertEqual(prime_implicants(2,[1,0,1,'X']),['-0','1-'])
        self.assertEqual(prime_implicants(2,[1,'X',1,'X']),['--'])
        self.assertEqual(prime_implicants(1,[0,'X']),[])
        self.assertEqual(prime_implicants(1,[1,0]),['0'])
        
    def test_minFunc(self):
        '''
        Each of the Test case has been personally verified and also verified using other tools. In some cases, the number of solutions provided by minFunc is lesser than the ones provided by other tools. On manual testing, it was found that the solutions provided by minFunc used lesser number of literals as compared to the ones provided by other tools(minFunc treats "w" and "w'" as separate literals, as "w'" needs to be computed separately, therefore increasing the number of gates required, and therefore the cost of implementation), and therefore, didn't result in a loss of any solutions.
        '''
        
        #Testing of 4 variable Functions with don't cares
        self.assertEqual(minFunc(4, '(3,6,10,13) d (0,2,5,7,8,9,12)'), "w'y+wy'+x'z'")
        self.assertEqual(minFunc(4, '(0,1) d (2,3,4,5,6,8,9,10,12,13,14)'), "y'")
        self.assertEqual(minFunc(4, '(6,11) d (0,3,4,5,8,10,12,14)'), "wx'y+xz' OR x'yz+xz'")
        self.assertEqual(minFunc(4, '(0,2,5,6,11,13) d (1,3,7,9,10,12,14,15)'), "w'x'+y+z")
        self.assertEqual(minFunc(4, '(3,9,12,15) d (0,1,4,7,8,10,11,14)'), "wx'+wz'+yz OR wy+wz'+x'z OR wz'+x'z+yz OR x'y'+y'z'+yz OR x'z+y'z'+yz")
        self.assertEqual(minFunc(4, '(1,2,3,7,9,11,12,14) d (0,6,13,15)'), "w'y+wx+x'z")
        self.assertEqual(minFunc(4, '(1,2,8,10,15) d (0,4,6,11,12)'), "w'x'y'+wyz+x'z'")
        self.assertEqual(minFunc(4, '(2,8,10,12) d (1,3,4,6,7,9,11,13,15)'), "wy'+x'y")
        
        #Testing of 4 variable Functions without Don't cares
        self.assertEqual(minFunc(4, '(0,1,2,4,5,6,8,9,12,13,14) d -'), "w'z'+xz'+y'")
        self.assertEqual(minFunc(4, '(1,2,4,5,6,10,11,12,13) d -'), "w'y'z+w'yz'+wx'y+xy'")
        self.assertEqual(minFunc(4, '(2,3,4,5,8,9,10,15) d -'), "w'x'y+w'xy'+wx'y'+wx'z'+wxyz OR w'x'y+w'xy'+wx'y'+wxyz+x'yz'")
        self.assertEqual(minFunc(4, '(0,1,4,5,7,9,10,11,13,15) d -'), "w'y'+wx'y+wz+xz OR w'y'+wx'y+xz+y'z")
        
        #Testing of 3 variable Functions with Don't Cares
        self.assertEqual(minFunc(3, '(3,4,7) d (1,2,5,6)'), 'w+x OR w+y')
        self.assertEqual(minFunc(3, '(5) d (2,3,6)'), "wx'y")
        self.assertEqual(minFunc(3, '(0,5) d (2,3,4)'), "wx'+x'y'")
        self.assertEqual(minFunc(3, '(0,1,5,7) d (6)'), "w'x'+wy")
        self.assertEqual(minFunc(3, '(2,5) d (0,4,6)'), "wx'+y'")
        self.assertEqual(minFunc(3, '(3,5) d (1,2,6)'), "w'y+x'y")
        
        #Testing of 3 variable Functions without Don't Cares
        self.assertEqual(minFunc(3, '(3) d -'), "w'xy")
        self.assertEqual(minFunc(3, '(2,3,6,7) d -'), "x")
        self.assertEqual(minFunc(3, '(0,1,2,3,7) d -'), "w'+xy")
        self.assertEqual(minFunc(3, '(0,1,2,5,6,7) d -'), "w'x'+wy+xy' OR w'y'+wx+x'y")
        self.assertEqual(minFunc(3, '(0,3,4,5,7) d -'), "wx'+x'y'+xy OR wy+x'y'+xy")
        
        #Testing of 2 variable Functions with Don't Cares
        self.assertEqual(minFunc(2, '() d (0)'), "0")
        self.assertEqual(minFunc(2, '(1,2) d (3)'), "w+x")
        self.assertEqual(minFunc(2, '(1) d (0,3)'), "w' OR x")
        self.assertEqual(minFunc(2, '(3) d (0)'), "wx")
        
        #Testing of 2 variable Functions without Don't Cares
        self.assertEqual(minFunc(2, '(1,2) d -'), "w'x+wx'")
        self.assertEqual(minFunc(2, '(3) d -'), "wx")
        
        #Testing of single variable functions
        self.assertEqual(minFunc(1, '(1) d (0)'), "1")
        self.assertEqual(minFunc(1, '(0,1) d -'), "1")
        self.assertEqual(minFunc(1, '(0) d -'), "w'")
        
        #Border Cases - Zero Function
        self.assertEqual(minFunc(4, '() d -'), '0')
        self.assertEqual(minFunc(3, '() d -'), '0')
        self.assertEqual(minFunc(2, '() d -'), '0')
        self.assertEqual(minFunc(1, '() d -'), '0')
        self.assertEqual(minFunc(4, '() d (1,4,9,15)'), '0')
        self.assertEqual(minFunc(3, '() d (0,3,7)'), '0')
        self.assertEqual(minFunc(2, '() d (2,3)'), '0')
        self.assertEqual(minFunc(1, '() d (1)'), '0')
        
        #Border Cases - One Function
        self.assertEqual(minFunc(4, '(0,1,2,3,4,5,6) d (7,8,9,10,11,12,13,14,15)'), '1')
        self.assertEqual(minFunc(3, '(0,2,4,6) d (1,3,5,7)'), '1')
        self.assertEqual(minFunc(2, '(1,3) d (0,2)'), '1')
        self.assertEqual(minFunc(1, '(0) d (1)'), '1')
        
        #self.assertEqual(minFunc(6,'(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,61,62,63) d -'), '1')
                
if __name__=='__main__':
	unittest.main()
