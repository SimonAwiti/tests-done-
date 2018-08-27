import unittest
import re 

class passwordvalidator(unittest.TestCase):

    def test_lengt_of_password(self):
        accepted = []
        password = raw_input ("enter your password: ")
        if len(password) < 6:
            print ("password must have a minimum of 6 charachters")
            assert len(password)< 6, "password must have more than 6 charcters!"
    def test_max_length_of_password (self):
        accepted = []
        password = raw_input ("enter your password: ")
        elif len(password) > 12:
            print ("password must have a maximum of 12 charachers")
            assert len (password) > 12, "pasword has more than 12 characters!"
    def test_numbers_in_password (self):
        accepted = []
        password = raw_input ("enter your password: ")
        if re.search('[0-9]',password) is None:
            print ("Make sure your password has a number in it")
            assert re.search('[0-9]',password) is None, "password must contain a number in it!"
    def test_alphabets_in_password (self):
        accepted = []
        password = raw_input ("enter your password: ")
        if re.search('[a-z]',password) is None:
            print ("Make sure your password has alphabets in it")
            assert re.search('[a-z]',password) is None, "password must contain an alphabet in it!"
        
unittest.main ()
