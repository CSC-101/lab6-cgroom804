import data
import lab6
import unittest
from lab6 import swap_case, str_translate, histogram_letters


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_alphabetical_sort1(self):
        books = [data.Book(["Henry"],"Harry Potter"),
                 data.Book(["Larry"], "The Wild Things"),
                 data.Book(["Kieran"], "How to Live")]
        lab6.alphabetical_sort(books)
        expected = [data.Book(['Henry'], 'Harry Potter'),
                    data.Book(['Kieran'], 'How to Live'),
                    data.Book(['Larry'], 'The Wild Things')]
        self.assertEqual(books, expected)

    def test_alphabetical_sort2(self):
        books = [data.Book(["Homer"],"The Iliad"),
                 data.Book(["Homer"], "The Odyssey"),
                 data.Book(["Sophocles"], "Oedipus")]
        lab6.alphabetical_sort(books)
        expected = [data.Book(["Sophocles"], "Oedipus"),
                    data.Book(["Homer"],"The Iliad"),
                    data.Book(["Homer"], "The Odyssey")]
        self.assertEqual(books, expected)

    # Part 2
    def test_swap_case1(self):
        list = "Hello! Welcome to Cal Poly."
        result = swap_case(list)
        expected = "hELLO! wELCOME TO cAL pOLY."
        self.assertEqual(result, expected)

    def test_swap_case2(self):
        list = "Goodbye! Come back in 3 weeks."
        result = swap_case(list)
        expected = "gOODBYE! cOME BACK IN 3 WEEKS."
        self.assertEqual(result, expected)

    # Part 3
    def test_str_translate1(self):
        string = 'abcdcba'
        old = 'a'
        new = 'x'
        result = str_translate(string, old, new)
        expected = 'xbcdcbx'
        self.assertEqual(result, expected)

    def test_str_translate2(self):
        string = 'Hello Lauren'
        old = 'l'
        new = '1'
        result = str_translate(string, old, new)
        expected = 'He11o Lauren'
        self.assertEqual(result, expected)

    # Part 4
    def test_histogram_letters1(self):
        sentence = "This is a long sentence, but is it a very long sentence"
        result = histogram_letters(sentence)
        expected = {'This': 1, 'a': 2, 'but': 1, 'is': 2, 'it': 1, 'long': 2, 'sentence': 2, 'very': 1}
        self.assertEqual(result, expected)

    def test_histogram_letters2(self):
        sentence = "I am Cole, I am not Jon, and I wrote this code, not Jon"
        result = histogram_letters(sentence)
        expected = {'Cole': 1, 'I': 3, 'Jon': 2, 'am': 2, 'and': 1, 'code': 1, 'not': 2, 'this': 1, 'wrote': 1}
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
