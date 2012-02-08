import unittest
from PyDBMain import PyDBMain

class TestPyDBMain(unittest.TestCase):
    
    
    def setUp(self):
        self.pyDB = PyDBMain(debug=True)
        self.fmt1 = """INSERT INTO {0}({1}) VALUES({2});"""
        self.q1 = ("books","title,book_id","Database Systems,123123")
        
    def test_safe_query(self):
        print self.pyDB.safe_query(self.fmt1, *self.q1)
        
        
if __name__ == '__main__':
    unittest.main()


