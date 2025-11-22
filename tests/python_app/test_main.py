import unittest
from python_app.main import somma

class TestMain(unittest.TestCase):

    def test_somma(self):
        self.assertEqual(somma(1,1),2)

if __name__ == "__main__":
    unittest.main()