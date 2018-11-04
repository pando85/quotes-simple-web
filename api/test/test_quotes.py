import unittest

from quotes.quote import Quote


class TestInitQuote(unittest.TestCase):
    def setUp(self):
        self.quote_json = {'id': 1, 'author': 'foo', 'quote': 'lorem ipsum'}

    def test_overload(self):
        quote_overload = self.quote_json.copy()
        quote_overload.update({'foo': 'boo'})
        with self.assertRaises(TypeError) as expected_exception:
            Quote(**quote_overload)
        self.assertEqual(
            "__new__() got an unexpected keyword argument 'foo'",
            str(expected_exception.exception))

    def test_unload(self):
        quote_unload = self.quote_json.copy()
        quote_unload.pop('author')
        with self.assertRaises(TypeError) as expected_exception:
            Quote(**quote_unload)
        self.assertEqual(
            "__new__() missing 1 required positional argument: 'author'",
            str(expected_exception.exception))

    def test_load(self):
        quote = Quote(**self.quote_json)
        [self.assertEqual(self.quote_json[attr], getattr(quote, attr)) for attr in Quote.__slots__]


if __name__ == '__main__':
    unittest.main()
