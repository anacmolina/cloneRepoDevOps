import unittest
from desoper import cloneRepoDevOps


class Test_hello(unittest.TestCase):
    def test__working(self):
        self.assertEqual(cloneRepoDevOps.hello(),
                         'Hello, World!', True)


if __name__ == '__main__':
    unittest.main()
