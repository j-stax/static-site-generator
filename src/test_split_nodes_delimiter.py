import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import *

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bold_delimiter(self):
        bold_textnode = TextNode("This is a **bold** phrase.", "text")
        new_nodes = split_nodes_delimiter([bold_textnode], "**", "bold")
        expected_nodes = [TextNode("This is a ", "text", None), TextNode("bold", "bold", None), TextNode(" phrase.", "text", None)]
        self.assertEqual(new_nodes, expected_nodes)

    def test_italic_delimiter(self):
        node = TextNode("This text has an *italic* word.", "text")
        new_nodes = split_nodes_delimiter([node], "*", "italic")
        expected_nodes = [TextNode("This text has an ", "text"), TextNode("italic", "italic"), TextNode(" word.", "text")]
        self.assertEqual(new_nodes, expected_nodes)

    def test_multiple_inline_elements(self):
        node = TextNode("This text has a `code block` here, and another `code block` here.", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        expected_nodes = [TextNode("This text has a ", "text"), TextNode("code block", "code"), TextNode(" here, and another ", "text"),
                            TextNode("code block", "code"), TextNode(" here.", "text")]
        self.assertEqual(new_nodes, expected_nodes)
        
