#!/usr/bin/python

import hiker
import unittest

class TestHiker(unittest.TestCase):

    day_number = 5

    def test_friday13th(self):
        me = hiker.Hiker()
        self.assertEqual(TestHiker.day_number, int(me.weekday_of(1905, 1, 13)))

if __name__ == '__main__':
    unittest.main()
