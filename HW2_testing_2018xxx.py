import unittest
from HW2_2018xxx import minFunc
from HW2_2018xxx import dec_to_bin
from HW2_2018xxx import function_rep_as_list
from HW2_2018xxx import comm_expr
from HW2_2018xxx import is_adjacent
from HW2_2018xxx import func_list_of_prime_implicants

class testpoint(unittest.TestCase):
    def test_dec_to_bin(self):
        self.assertEqual(dec_to_bin(1,1),'1')
        self.assertEqual(dec_to_bin(2,2),'10')
        self.assertEqual(dec_to_bin(3,5),'101')
        self.assertEqual(dec_to_bin(4,15),'1111')
    
    def test_function_rep_as_list(self):
        self.assertEqual(function_rep_as_list(1,'(0) d()'), [1,0])
        self.assertEqual(function_rep_as_list(2,'(2) d(1)'), [0,'X',1,0])
        self.assertEqual(function_rep_as_list(3,'(5,3) d(7)'), [0,0,0,1,0,1,0,'X'])
        self.assertEqual(function_rep_as_list(4,'(1,7,3,14) d(2,6)'), [0,1,'X',1,0,0,'X',1,0,0,0,0,0,0,1,0])
        self.assertEqual(function_rep_as_list(3,'(0,2,4) d(7)'), [1,0,1,0,1,0,0,'X'])
    
    def test_comm_expr(self):
        self.assertEqual(comm_expr('0010', '0000', '-'),'00-0')
        self.assertEqual(comm_expr('001', '000', '-'),'00-')
        self.assertEqual(comm_expr('--1-', '--0-', '-'),'----')
        self.assertEqual(comm_expr('1-', '0-', '-'),'--')
        self.assertEqual(comm_expr('01', '00', '-'),'0-')
    
    def test_is_adjacent(self):
        self.assertEqual(is_adjacent('000','010'), True)
        self.assertEqual(is_adjacent('--0','--1'), True)
        self.assertEqual(is_adjacent('-0-','-01'), False)
        self.assertEqual(is_adjacent('0','1'), True)
        self.assertEqual(is_adjacent('011','111'), True)
        self.assertEqual(is_adjacent('-1-','-0-'), True)
        self.assertEqual(is_adjacent('-1-','-01'), False)
        self.assertEqual(is_adjacent('0','1'), True)
        self.assertEqual(is_adjacent('00-0','0-01'), False)
        
    def test_func_list_of_prime_implicants(self):
        self.assertEqual(func_list_of_prime_implicants(4,['0000','0001','0010','0100','0101','1000','1001','1100','1101','1110']),['--0-','00-0','11-0'])
        self.assertEqual(func_list_of_prime_implicants(4,['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']),['----'])
        self.assertEqual(func_list_of_prime_implicants(4,['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110']),['---0','--0-','-0--','0---'])
        self.assertEqual(func_list_of_prime_implicants(4,['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110']),['---0','--0-','-0--','0---'])
        self.assertEqual(func_list_of_prime_implicants(3,['000','001','010','011','100','101','110','111']),['---'])
        self.assertEqual(func_list_of_prime_implicants(3,['011','101','110']),['011','101','110'])
        self.assertEqual(func_list_of_prime_implicants(2,['00','01','10','11']),['--'])
        
    def test_minFunc(self):
        None
                
if __name__=='__main__':
	unittest.main()
