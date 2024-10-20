import unittest

from textnode import *
from textnode_to_htmlnode import text_node_to_html_node
from leafnode import LeafNode

class TestTextNodeToHtml(unittest.TestCase):
    def test_leafnode_instance(self):
        textnode = TextNode(text="This is a bold node.", text_type="bold")
        self.assertTrue(isinstance(text_node_to_html_node(textnode), LeafNode))

    def test_link_textnode_to_html(self):
        textnode = TextNode(text="This is a link node.", text_type="link", url="https://link.com")
        self.assertEqual(text_node_to_html_node(textnode).to_html(), "<a href=\"https://link.com\">This is a link node.</a>")

    def test_image_textnode_to_html(self):
        textnode = TextNode(text="cat picture", text_type="image", url="images/cat_pic.png")
        self.assertEqual(text_node_to_html_node(textnode).to_html(), "<img src=\"images/cat_pic.png\" alt=\"cat picture\" />")