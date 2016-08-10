class TestCaseClass:
    """class for all the test cases which needs to be verified"""

    def __init__(self):
        # Sample Data
        self.message = 'canyoudecryptthismessage?'          
                
    def test_rowLength(self,columns):
        # test to get the round of value of each row
        rows_length = int(round(len(self.message) / float(columns))) 
        return rows_length
   
    def test_reverseList(self):
        # test to get the reverse string
        output = self.message[::-1]
        return output
        

import unittest
class TestSequenceFunctions(unittest.TestCase):
    '''Unit test for testing the code with sample data'''
    
    def setUp(self):    
        '''Created the class object'''
        self.test = TestCaseClass()
    
    def test_functional(self):
        '''Test the cases by changing the sample data and output'''        
        
        self.assertEqual(self.test.test_rowLength(7), 4)
        self.assertEqual(self.test.test_reverseList(), '?egassemsihttpyrceduoynac')
        

if __name__ == '__main__':
    unittest.main()
