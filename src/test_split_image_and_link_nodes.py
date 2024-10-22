import unittest

from split_image_and_link_nodes import *
from textnode import *

class TestSplitImageAndLinkNodes(unittest.TestCase):
    def test_split_nodes_images(self):
        node = TextNode(
            "This is text with images ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", 
            TextType.TEXT,
        )
        result_list = split_nodes_images([node])
        expected_result = [
            TextNode("This is text with images ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertEqual(result_list, expected_result)

    def test_multiple_image_nodes(self):
        node1 = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", 
            TextType.TEXT,
        )
        node2 = TextNode(
            "This is another text with a ![some alt text](https://www.image.png) and ![another alt text](https://node2.image.jpeg) image markdown.", 
            TextType.TEXT,
        )
        result = split_nodes_images([node1, node2])
        expected_result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("This is another text with a ", TextType.TEXT),
            TextNode("some alt text", TextType.IMAGE, "https://www.image.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("another alt text", TextType.IMAGE, "https://node2.image.jpeg"),
            TextNode(" image markdown.", TextType.TEXT)
        ]
        self.assertEqual(result, expected_result)


    def test_split_nodes_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        result = split_nodes_links([node])
        expected_result = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(result, expected_result)

    def test_multiple_link_nodes(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        node2 = TextNode(
            "This is a second text with a link [to boot dev2](https://www.second.boot.dev) and a second [to youtube2](https://www.two.youtube.com/@bootdotdev) link markdown.",
            TextType.TEXT,
        )
        result = split_nodes_links([node, node2])
        expected_result = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            TextNode("This is a second text with a link ", TextType.TEXT),
            TextNode("to boot dev2", TextType.LINK, "https://www.second.boot.dev"),
            TextNode(" and a second ", TextType.TEXT),
            TextNode("to youtube2", TextType.LINK, "https://www.two.youtube.com/@bootdotdev"),
            TextNode(" link markdown.", TextType.TEXT)
        ]
        self.assertEqual(result, expected_result)

