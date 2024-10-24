import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        bold_node = LeafNode(tag="b", value="Bold text")
        textnode1 = LeafNode(tag=None, value="Normal text1")
        italic_node = LeafNode(tag="i", value="Italic text")
        textnode2 = LeafNode(tag=None, value="Normal text2")
        parentnode_p = ParentNode(tag="p", children=[bold_node, textnode1, italic_node, textnode2])
        self.assertEqual(parentnode_p.to_html(), "<p><b>Bold text</b>Normal text1<i>Italic text</i>Normal text2</p>")

    def test_nested_parentnode(self):
        italic_node = LeafNode(tag="i", value="Italic text")
        textnode2 = LeafNode(tag=None, value="Normal text2")
        parentnode_p = ParentNode(tag="p", children=[italic_node, textnode2])
        parentnode_div = ParentNode(tag="div", children=[parentnode_p])
        self.assertEqual(parentnode_div.to_html(), "<div><p><i>Italic text</i>Normal text2</p></div>")

    def test_nested_multiple_parentnodes(self):
        bold_node = LeafNode(tag="b", value="Bold text")
        textnode1 = LeafNode(tag=None, value="Normal text1")
        anchor_node = LeafNode(tag="a", value="Anchor text", props={ "href": "https://www.boot.dev"})
        italic_node = LeafNode(tag="i", value="Italic text")
        textnode2 = LeafNode(tag=None, value="Normal text2")
        parentnode_p1 = ParentNode(tag="p", children=[bold_node, textnode1, anchor_node])
        parentnode_p2 = ParentNode(tag="p", children=[italic_node, textnode2])
        parentnode_div = ParentNode(tag="div", children=[parentnode_p1, parentnode_p2])
        self.assertEqual(
            parentnode_div.to_html(), 
            "<div><p><b>Bold text</b>Normal text1<a href=\"https://www.boot.dev\">Anchor text</a></p>" \
            "<p><i>Italic text</i>Normal text2</p></div>"
        )

