import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import *

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bold_delimiter(self):
        bold_textnode = TextNode("This is a **bold** phrase.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([bold_textnode], "**", TextType.BOLD)
        expected_nodes = [TextNode("This is a ", "text", None), TextNode("bold", "bold", None), TextNode(" phrase.", TextType.TEXT, None)]
        self.assertEqual(new_nodes, expected_nodes)

    def test_italic_delimiter(self):
        node = TextNode("This text has an *italic* word.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected_nodes = [TextNode("This text has an ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" word.", TextType.TEXT)]
        self.assertEqual(new_nodes, expected_nodes)

    def test_multiple_inline_elements(self):
        node = TextNode("This text has a `code block` here, and another `code block` here.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [TextNode("This text has a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" here, and another ", TextType.TEXT),
                            TextNode("code block", TextType.CODE), TextNode(" here.", TextType.TEXT)]
        self.assertEqual(new_nodes, expected_nodes)

    def test_no_delimiter(self):
        node = TextNode("This text has no delimiter.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected_nodes = [node]
        self.assertEqual(new_nodes, expected_nodes)
        
