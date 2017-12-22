from ut import *

if __name__ == '__main__':
    import unittest


    class TestFactorialMethods(unittest.TestCase):
        def test_normal_values(self):
            self.assertEqual(fact(5), 120)
            self.assertEqual(fact(0.5), None)
            self.assertEqual(fact(-5), None)

        def test_except_ValueError(self):
            with self.assertRaises(ValueError):
                fact(-1)

        def test_except_TypeError(self):
            with self.assertRaises(TypeError):
                fact([0, 1])
            with self.assertRaises(TypeError):
                fact('hello')
            with self.assertRaises(TypeError):
                fact(0.5)


unittest.main()