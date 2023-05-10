import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase): #best to name class related to function you're testing: use Test in name
    """Tests for 'name_function.py' """

    def test_first_last_name(self): #method tests one aspect of get_formatted_name; run automatically b/c name test
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
        #assert methods verify result you received matches result you expected

if __name__ == '__main__': #looks at special variable __name__, set when program is executed
    unittest.main() #if file being run is a main program, value of __name__ is set to __main__
                    # in this case, unittest.main() is called, which run the test cases
                    #when testing frmework imports this files, the value of __name__ won't 
                    #be __main__ and block will not execute