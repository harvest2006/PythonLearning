#测试代码
import unittest
from  name_function import get_formatted_name
class NamesTestCase(unittest.TestCase):
    '''测试name_function.py'''
    def test_first_last_name(self):
        '''能够正确处理像Janis Joplin这样的名字吗？'''
        formatted_name=get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')
    def test_first_middle_last_name(self):
        '''能够正确处理像 Wolfgang Amadeus Mozart这样的名字吗？'''
        formatted_name=get_formatted_name('wolfgang','amadeus','mozart')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')
unittest.main