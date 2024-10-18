import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        props_dict = {
            "font-family": "Consolas, Monospace",
            "color": "blue"
        }
        props_dict2 = {
            "href": "https://www.boot.dev",
            "target": "_blank"
        }
        html_node = HTMLNode("h1", "This is heading1", props=props_dict)
        html_node2 = HTMLNode("a", props=props_dict2)
        self.assertEqual(html_node.props_to_html(), " font-family=\"Consolas, Monospace\" color=\"blue\"")
        self.assertEqual(html_node2.props_to_html(), " href=\"https://www.boot.dev\" target=\"_blank\"")
