import unittest
import script

class TestMain(unittest.TestCase):

    def setUp(self):
        print('Sto per far girare una funzione')
    def test_input(self):
        result = script.run_guess(5,5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = script.run_guess(5, 6)
        self.assertFalse(result)

    def test_input_not_in_range(self):
        result = script.run_guess(12, 2)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        with self.assertRaises(ValueError) as context:
            result = script.run_guess('abc', 2)
        self.assertEqual(str(context.exception), "Per favore inserisci un numero valido")


if __name__ == '__main__':
    unittest.main()