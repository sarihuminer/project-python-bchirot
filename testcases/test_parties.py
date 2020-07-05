import unittest
import party

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(party.Party.get_max_Party(self), 67)
        self.assertEqual(party.Party.get_all_Over_Parties(self),9)


if __name__ == '__main__':
    unittest.main()
