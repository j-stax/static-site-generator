import unittest

from markdown_to_html_node import *
from htmlnode import HTMLNode

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_basic_markdown(self):
        md = "This is a p block text and a ![rick roll](https://i.imgur.com/aKaOqIh.gif) image.\n\n" \
                "1. This is a ol markdown.\n2. Another ol markdown."
        result = markdown_to_html_node(md)
        expected_result = HTMLNode(
            tag="div",
            value=None,
            children=[
                HTMLNode(
                    tag="p", 
                    value="This is a p block text and a ![rick roll](https://i.imgur.com/aKaOqIh.gif) image.", 
                    children=[
                        HTMLNode(
                            tag="img",
                            value="",
                            children=None,
                            props={'src': 'https://i.imgur.com/aKaOqIh.gif', 'alt': 'rick roll'}
                        )
                    ],
                ), 
                HTMLNode(
                    tag="ol",
                    value="This is a ol markdown.\nAnother ol markdown.",
                    children=None,
                )
            ],
        )
        self.assertEqual(print(result), print(expected_result))

    def test_multiple_nested_nodes(self):
        md = "## This is an h2 heading.\n\n" \
            ">This is a quote block with a [link to boot.dev](https://www.boot.dev) link.\n\n" \
            "* One unordered list item.\n* And another unordered list item."
        result = markdown_to_html_node(md)
        expected_result = HTMLNode(
            tag="div",
            value="Some value",
            children=[
                HTMLNode(
                    tag="h2",
                    value="This is an h2 heading.",
                    children=None,
                    props=None
                ),
                HTMLNode(
                    tag="blockquote",
                    value="This is a quote block with a [link to boot.dev](https://www.boot.dev) link.",
                    children=[
                        HTMLNode(
                            tag="a",
                            value="link to boot.dev",
                            children=None,
                            props={'href': 'https://www.boot.dev'}
                        )
                    ]
                ),
                HTMLNode(
                    tag="ul",
                    value="One unordered list item.\nAnd another unordered list item.",
                    children=None,
                    props=None
                )
            ],
            props=None
        )
        self.assertEqual(print(result), print(expected_result))
