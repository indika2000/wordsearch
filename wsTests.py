__author__ = 'Indy'

import unittest
from wordsearch import WordSearch

class WordSearchTest(unittest.TestCase):

    skiptest = False

    def setUp(self):
        self.wordmatrix = [['w', 'a', 'b', 'c'], ['g', 'c', 'a', 't'], ['u', 'x', 't', 'y'], ['m', 'u', 'e', 's']]
        self.wordsearch = WordSearch(self.wordmatrix)

    def test_word_search_find_cats(self):
        expectedresult = [[0,0,0,1], [0,0,2,0], [0,0,3,0], [0,0,0,4]]
        self.assertListEqual(self.wordsearch.findword('cats'), expectedresult)


    @unittest.skipIf(skiptest is True, "Skipping as cats test failed")
    def test_word_search_find_bats(self):
        pass

    @unittest.skipIf(skiptest is True, "Skipping as cats test failed")
    def test_word_search_find_gum(self):
        pass

    @unittest.skipIf(skiptest is True, "Skipping as cats test failed")
    def test_word_search_find_mutes(self):
        pass


if __name__ == '__main__':
    unittest.TestCase()