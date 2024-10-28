import unittest

from generate_page import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_h1_found(self):
        md = """
# This is an h1 header.

"""
        text = extract_title(md)
        self.assertEqual(text, "This is an h1 header.")


    def test_exception_raised(self):
        md = """
This is not an h1 header.
"""
        with self.assertRaises(ValueError):
            extract_title(md)