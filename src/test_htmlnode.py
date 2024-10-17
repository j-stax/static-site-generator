import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props_dict = {
            "font-family": "Consolas, Monospace",
            "color": "blue"
        }
        html_node = HTMLNode("h1", "This is heading1", props=props_dict)
        self.assertEquals(html_node.props_to_html(), " font-family=\"Consolas, Monospace\" color=\"blue\"")