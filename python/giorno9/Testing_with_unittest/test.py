import unittest
import main

class TestMain(unittest.TestCase):

    def setUp(self):
        print('Sto per far girare una funzione')
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'dsfssdf'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

    def test_do_stuff5(self):
        test_param = 0
        result = main.do_stuff(test_param)
        self.assertEqual(result, 5)

    def tearDown(self):
        print('pulisco tutto')

# Il comando si chiama con main a prescindere dal nome del modulo che stiamo testando

# Visto che non vogliamo che questo file giri in altre situazioni possiamo usare:

if __name__ == 'main':
    unittest.main()