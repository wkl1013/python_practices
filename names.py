from name_function import get_formatted_name

# 导入测试类 unittest
import unittest

class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):

        formatted_name = get_formatted_name('Mike', "Json")
        self.assertEqual(formatted_name, 'Mike Json')

if __name__ == "__main__":
    unittest.main()