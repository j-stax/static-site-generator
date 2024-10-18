import unittest

from leafnode import *

class TestLeafNode(unittest.TestCase):

    def test_leafnode_to_html(self):
        leafnode = LeafNode(tag="a", value="This is an anchor tag", props={ "href": "https://www.boot.dev" })
        self.assertEqual(leafnode.to_html(), "<a href=\"https://www.boot.dev\">This is an anchor tag</a>")

    def test_leafnode_value(self):
        leafnode = LeafNode(tag="p", value="", props=None)
        with self.assertRaises(ValueError):
            leafnode.to_html()

    def test_no_tag(self):
        leafnode = LeafNode(value="This is raw text.", props=None)
        self.assertEqual(leafnode.to_html(), "This is raw text.")


        