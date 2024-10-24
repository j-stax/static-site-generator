import unittest

from inline_markdown import text_to_textnode
from textnode import *

class TestTextToTextnode(unittest.TestCase):
    def test_basic_md_text(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnode(text)
        expected_result = [
            TextNode("This is ", TextType.TEXT, None), 
            TextNode("text", TextType.BOLD, None), 
            TextNode(" with an ", TextType.TEXT, None), 
            TextNode("italic", TextType.ITALIC, None), 
            TextNode(" word and a ", TextType.TEXT, None), 
            TextNode("code block", TextType.CODE, None), 
            TextNode(" and an ", TextType.TEXT, None), 
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"), 
            TextNode(" and a ", TextType.TEXT, None), 
            TextNode("link", TextType.LINK, "https://boot.dev")
        ]
        self.assertEqual(result, expected_result)

    def test_random_ordered_markdown(self):
        text = "This is *text* with a [link](https://boot.dev), a ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"
        text += " and a `code block` as well as a **bold word**."
        result = text_to_textnode(text)
        expected_result = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.ITALIC),
            TextNode(" with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode(", a ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" as well as a ", TextType.TEXT),
            TextNode("bold word", TextType.BOLD),
            TextNode(".", TextType.TEXT)
        ]
        self.assertEqual(result, expected_result)